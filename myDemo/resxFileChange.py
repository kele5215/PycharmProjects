# -*- coding:UTF-8-*-

import os
import shutil
from chardet.universaldetector import UniversalDetector


def find_resx_file(path_name):
    """
    path_nameから指定するファイルの接尾語ファイル名リストを返す

    :param path_name: 接尾語を判別したいフォルダ
    :return: ファイル名リスト
    """
    # 戻すリスト
    result_list_file = []

    # 接尾語定義
    # suffix = ('.st', '.js', '.cs')
    # suffix = ('.sql', '.cmd')
    suffix = ('.resx')
    '''
    指定接尾語ファイルを取得してリストに設定する
    '''
    for maindir, subdir, file_name_list in os.walk(path_name):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            ext = os.path.splitext(apath)[1]

            if ext in suffix:
                result_list_file.append(apath)
    '''
    テストため、取得されたファイルをddd.textに出力する
    '''
    new_line_list = '\n'.join(result_list_file)
    base_dir = os.path.dirname(__file__)
    out_file = os.path.join(base_dir, 'aaa.txt')
    with open(out_file, 'a+', encoding='utf-8') as f_out:
        f_out.writelines(new_line_list)

    return result_list_file


if __name__ == '__main__':

    # 目標フォルダ初期化
    src_folder = r'C:\work\developer\3.1.4JP(A-Law)'

    # 目標フォルダ配下から指定接尾語ファイルを取得する
    result_list_file = find_resx_file(src_folder)
