# -* - coding: UTF-8 -* -
import os
from inieditor import IniEditor


def load_ini(locationini):
    #  ------------------------------------------------------------------------
    #  指定パスのチェック設定
    #  ------------------------------------------------------------------------
    if len(locationini) == 0:
        current_path = os.path.dirname(os.path.realpath(__file__))
        print(current_path)
        locationini = os.path.join(current_path, "setting.ini")

    #  ------------------------------------------------------------------------
    #  指定キーワードで対応値を戻す
    #  ------------------------------------------------------------------------
    ini_editor = IniEditor(locationini)
    sensitivity_vad_bic = float(ini_editor.get_profile_str("Parameters", "mt"))
    print(sensitivity_vad_bic)

    #  ------------------------------------------------------------------------
    #  指定セクションで対応ディクショナリを戻す
    #  ------------------------------------------------------------------------
    param_dict = ini_editor.get_profile_dict("Parameters")
    for k, v in param_dict.items():
        print("{0} : {1}".format(k, v))
    # print(param_dict)
    print(param_dict["fnparam"])

    #  ------------------------------------------------------------------------
    #  指定キーワードで対応値を修正
    #  ------------------------------------------------------------------------
    ini_editor = IniEditor(locationini)
    ini_editor.modify_profile_str("Parameters", "mt", "99999")

    # 修正後再取り込み
    sensitivity_vad_bic = float(ini_editor.get_profile_str("Parameters", "mt"))
    print(sensitivity_vad_bic)

    #  ------------------------------------------------------------------------
    #  指定キーワードで対応値を追加
    #  ------------------------------------------------------------------------
    ini_editor = IniEditor(locationini)
    ini_editor.modify_profile_str("Parameters", "mtyyyyyy", "5555")

    # 修正後再取り込み
    sensitivity_vad_bic = float(
        ini_editor.get_profile_str("Parameters", "mtyyyyyy"))
    print(sensitivity_vad_bic)

    ini_editor = IniEditor(locationini)
    ini_editor.modify_profile_str("ParametersXXXX", "mtyyyyyy", "66666")

    # 修正後再取り込み
    sensitivity_vad_bic = float(
        ini_editor.get_profile_str("ParametersXXXX", "mtyyyyyy"))
    print(sensitivity_vad_bic)

    #  ------------------------------------------------------------------------
    #  指定キーワードで対応値を削除
    #  ------------------------------------------------------------------------
    ini_editor = IniEditor(locationini)
    del_result = ini_editor.del_profile_str("ParametersXXXX", "mtyyyyyy")


def main():
    # load_ini(r"C:\work\developer\20181026-SpeakerSegregationJar\SpeakerSegregation\setting.ini")
    load_ini("")


if __name__ == "__main__":
    main()
