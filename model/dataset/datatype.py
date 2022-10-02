from __future__ import annotations


class Information:
    """問題作成に関する情報を管理するクラス
    """

    def __init__(self) -> None:
        # 読みデータ数
        self.nspeech = 0
        # 読みデータ
        self.speech = []
        # サンプル単位の開始位置
        self.offset = []
        # サンプル単位の冒頭の削除量
        self.begin = []
        # サンプル単位の末尾の削除量
        self.end = []
        # 合成前の冒頭、末尾を削除した読みデータのサンプル数
        self.before_synthesize_length = []
        # 合成後の問題データのサンプル数
        self.problem_length = 0
        # 分割数
        self.nsplit = 0
        # サンプル単位の分割長
        self.duration = []

    def set_information(self, nspeech:int, speech:list, offset:list[int], begin:list[int], end:list[int],
                        before_synthesize_length:list[int], problem_length:int, nsplit:int, duration:list[int]) -> None:
        """問題作成に必要な情報のセッター

        Args:
            nspeech (int): 読みデータ数
            speech (list): 読みデータ
            offset (list[int]): サンプル単位の開始位置
            begin (list[int]): サンプル単位の冒頭の削除量
            end (list[int]): サンプル単位の末尾の削除量
            before_synthesize_length (list[int]): 合成前の冒頭、末尾を削除した読みデータのサンプル数
            problem_length (int): 合成後の問題データのサンプル数
            nsplit (int): 分割数
            duration (list[int]): サンプル単位の分割長
        """

        self.nspeech = nspeech
        self.speech = speech
        self.offset = offset
        self.begin = begin
        self.end = end
        self.before_synthesize_length = before_synthesize_length
        self.problem_length = problem_length
        self.nsplit = nsplit
        self.duration = duration
