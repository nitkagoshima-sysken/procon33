from __future__ import annotations
import asyncio
import aiohttp
import requests
import wave
import json


HOST = ''
TOKEN = ''
HEADER = {
    'procon-token': TOKEN
}


def async_runner(fn: function) -> function:
    """非同期な関数を受け取り、その関数を非同期に実行する関数を返す

    Args:
        fn (function): 非同期な関数
    """
    def wrapper(*args, **kwargs):
        loop = asyncio.get_event_loop()
        value = loop.run_until_complete(fn(*args, **kwargs))
        return value
    return wrapper


async def get_match() -> tuple[bool, dict | str]:
    """試合の情報を取得する

    Returns:
        tuple[bool, dict | str]:
        リクエストが成功したかのboolとレスポンスを返す
        リクエスト成功時はレスポンスとして以下のプロパティを含むdictを返す
        problems: 試合中の問題数。整数
        bonus_factor: 使用した分割数に対するボーナス係数の配列。n番目がn個利用場合のボーナス係数。
        penalty: 変更札に適用される係数。整数
        リクエスト失敗時はレスポンスとしてその概要のstrを返す
    """
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(HOST + '/match', headers=HEADER, ssl=True) as res:
                if res.status == requests.codes.ok:
                    data = await res.json()
                    success = True
                else:
                    data = await res.text()
                    success = False
                return (success, data)
        except Exception as err:
            print(err)


async def get_problem() -> tuple[bool, dict | str]:
    """問題情報を取得する

    Returns:
        tuple[bool, dict | str]:
        リクエストが成功したかのboolとレスポンスを返す
        リクエスト成功時はレスポンスとして以下のプロパティを含むdictを返す
        id: 問題ID
        chunks: 分割数。整数
        start_at: 開始時間のunixtime
        time_limit: 制限時間。単位は秒。整数
        data: 重ね合わせ数。整数
        リクエスト失敗時はレスポンスとしてその概要のstrを返す
    """
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(HOST + '/problem', headers=HEADER, ssl=True) as res:
                if res.status == requests.codes.ok:
                    data = await res.json()
                    success = True
                else:
                    data = await res.text()
                    success = False
                return (success, data)
        except Exception as err:
            print(err)


async def get_chunk(n_chunk: int) -> tuple[bool, dict | str]:
    """取得する分割データの数を指定する

    Args:
        n_chunk (int): 取得する分割データの数

    Returns:
        tuple[bool, dict | str]:
        リクエストが成功したかのboolとレスポンスを返す
        リクエスト成功時はレスポンスとして以下のプロパティを含むdictを返す
        chunks: 各分割データのファイル名の配列
        リクエスト失敗時はレスポンスとしてその概要のstrを返す
    """
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(HOST + '/problem/chunks?n=' + str(n_chunk), headers=HEADER, ssl=True) as res:
                if res.status == requests.codes.ok:
                    data = await res.json()
                    success = True
                else:
                    data = await res.text()
                    success = False
                return (success, data)
        except Exception as err:
            print(err)


async def get_file(file_name: str, save_path: str) -> tuple[bool, bytes | str]:
    """wavの取得を行う

    Args:
        file_name (str): 取得するwavファイルの名前
        save_path (str): 取得したファイルを保存するパス

    Returns:
        tuple[bool, bytes | str]:
        リクエストが成功したかのboolとレスポンスを返す
        リクエスト成功時はレスポンスとしてwavファイルのデータを返す
        リクエスト失敗時はレスポンスとしてその概要のstrを返す
    """
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(HOST + '/problem/chunks/' + file_name, headers=HEADER, ssl=True) as res:
                if res.status == requests.codes.ok:
                    data = await res.read()
                    success = True
                    with wave.open(save_path + file_name, mode='wb') as f:
                        f.setnchannels(1)
                        f.setsampwidth(2)
                        f.setframerate(48000)
                        f.writeframes(bytes(data))
                else:
                    data = await res.text()
                    success = False
                return (success, data)
        except Exception as err:
            print(err)


async def answer(problem_id: str, answers: list[str]) -> tuple[bool, dict | str]:
    """問題への回答を送信する

    Args:
        problem_id (str): 問題ID
        answers (list[str]): 回答する絵札のIDの文字列の配列。各絵札のIDは配布された音声の0埋めされた2桁の数字の部分

    Returns:
        tuple[bool, dict | str]:
        リクエストが成功したかのboolとレスポンスを返す
        リクエスト成功時はレスポンスとして以下のプロパティを含むdictを返す
        problem_id: 問題ID
        answers: 解凍された絵札のIDの配列
        accepted_at: 回答を受信した日時のunix time
        リクエスト失敗時はレスポンスとしてその概要のstrを返す
    """

    body = json.dumps({'problem_id': problem_id, 'answers': answers})

    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(HOST + '/problem', data=body, headers=HEADER, ssl=True) as res:
                if res.status == requests.codes.ok:
                    data = await res.json()
                    success = True
                else:
                    data = await res.text()
                    success = False
                return (success, data)
        except Exception as err:
            print(err)
