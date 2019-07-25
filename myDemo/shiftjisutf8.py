# -*- coding:UTF-8-*-

import os
import shutil
from chardet.universaldetector import UniversalDetector


def find_sql_cmd(path_name):
    """
    path_nameから指定するファイルの接尾語ファイル名リストを返す

    :param path_name: 接尾語を判別したいフォルダ
    :return: ファイル名リスト
    """
    # 戻すリスト
    result_list_file = []

    # 接尾語定義
    # suffix = ('.st', '.js', '.cs')
    suffix = ('.sql', '.cmd')
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
    テストため、取得されたファイルをa.textに出力する
    '''
    # new_line_list = '\n'.join(result_list_file)
    # base_dir = os.path.dirname(__file__)
    # out_file = os.path.join(base_dir, 'aaa.txt')
    # with open(out_file, 'a+', encoding='utf-8') as f_out:
    #     f_out.writelines(new_line_list)

    return result_list_file


def detect_character_code(file_list):
    """
    file_listから該当するファイルの文字コードを判別して
    ファイル名と文字コードのdictを返す

    :param file_list: 文字コードを判別したいファイルリスト
    :return: ファイル名がキー、文字コードが値のdict
    """

    files_code_dic = {}
    detector = UniversalDetector()
    for file in file_list:
        with open(file, 'rb') as f_in:
            detector.reset()
            for line in f_in.readlines():
                detector.feed(line)
                if detector.done:
                    break
            detector.close()
            files_code_dic[file] = detector.result['encoding']
    '''
    テストため、取得されたファイルをb.textに出力する
    '''
    # base_dir = os.path.dirname(__file__)
    # out_file = os.path.join(base_dir, 'bbb.txt')
    # with open(out_file, 'a+', encoding='utf-8') as f_out:
    #     for key, value in files_code_dic.items():
    #         f_out.write('{0}\t{1}'.format(key, value))
    #         f_out.write('\n')

    return files_code_dic


def change_character_code(file_dict):
    """
    file_dictから該当するファイルの文字コードを判別して
    ファイル名の文字コードを変換する

    :param file_dict: 文字コードを判別したいファイルリスト
    """
    # 文字コード初期定義
    endcode = ('ascii', 'SHIFT_JIS')

    # 変換されたファイル出力用リスト
    change_character_file = []

    for key, value in file_dict.items():
        if value in endcode:
            # 出力用リストを追加する
            change_character_file.append(key)

            # 元ファイルをコピーする再度命名
            new_file_name = os.path.splitext(
                key)[0] + '_old' + os.path.splitext(key)[1]
            shutil.copyfile(key, new_file_name)

            # 元ファイルを削除する
            os.unlink(key)

            # 文字コード変換処理を行う
            with open(key, 'w', encoding='UTF-8-SIG') as f_out:
                with open(new_file_name, 'r', encoding=file_dict[key]) as f_in:
                    f_out.write(f_in.read())

            # 正常の場合、コピーされたファイルを削除する
            os.unlink(new_file_name)
    '''
    テストため、変換されたファイルをc.textに出力する
    '''
    new_line_list = '\n'.join(change_character_file)
    base_dir = os.path.dirname(__file__)
    out_file = os.path.join(base_dir, 'ccc.txt')
    with open(out_file, 'a+', encoding='utf-8') as f_out:
        f_out.writelines(new_line_list)

    return change_character_file


if __name__ == '__main__':

    # 目標フォルダ初期化
    src_folder = r'C:\Users\h-zhang\Desktop\temp\新しいフォルダー\Database'

    # 目標フォルダ配下から指定接尾語ファイルを取得する
    result_list_file = find_sql_cmd(src_folder)

    # 指定接尾語ファイルからファイルの文字コードを取得する
    files_code_dic = detect_character_code(result_list_file)

    # ファイルの文字コードを判定してUTF-8に変換する
    change_character_code(files_code_dic)
