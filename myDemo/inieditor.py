# -* - coding: UTF-8 -* -
from configobj import ConfigObj


class IniEditor:
    """
    iniファイルの各属性値やヘルパー関数を保持する。

    Attributes
    ----------
    # pass
    """

    def __init__(self, inifile_path):
        """
        Parameters
        ----------
        inifile_path : str
            iniファイル(パスを含む)。
        """
        self.inifile_path = inifile_path

    def get_profile_str(self, section, keyword):
        """
        从ini配置文件中读取变量的值

        Parameters
        ----------
        section : str
            要获取的变量所在段名称
        keyword : str
            要获取的变量名称

        Returns
        -------
        value : str
            対象のキーの値。

        Raises
        ------
        IOError
            iniファイル読み込むエラー。
        """

        config = ConfigObj(self.inifile_path, encoding='UTF8')
        #  ------------------------------------------------------------------------
        #  指定キーワードで対応値を戻す
        #  ------------------------------------------------------------------------
        value = config[section][keyword]
        if value is not None and len(value) != 0:
            return value
        else:
            return False

    def get_profile_dict(self, section):
        """
        从ini配置文件中读取变量的值

        Parameters
        ----------
        section : str
            要获取的变量所在段名称

        Returns
        -------
        value : dict
            対象のキーの値。

        Raises
        ------
        IOError
            iniファイル読み込むエラー。
        """
        config = ConfigObj(self.inifile_path, encoding='UTF8')
        #  ------------------------------------------------------------------------
        #  指定セクションで対応ディクショナリを戻す
        #  ------------------------------------------------------------------------
        return config[section]

    def modify_profile_str(self, section, keyword, modify_value):
        """
        从ini配置文件中修正变量的值

        Parameters
        ----------
        section : str
            要获取的变量所在段名称
        keyword : str
            要修正的变量名称
        modify_value : str
            要修正的値

        Raises
        ------
        IOError
            iniファイル読み込むエラー。
        """

        config = ConfigObj(self.inifile_path, encoding='UTF8')
        #  ------------------------------------------------------------------------
        #  指定キーワードで対応値を修正
        #  ------------------------------------------------------------------------
        sect = config.keys()
        if section in sect:
            # 指定セクションが存在場合、修正する
            config[section][keyword] = modify_value
        else:
            # 指定セクションが存在しない、追加する
            config[section] = {}
            config[section][keyword] = modify_value
        config.write()

    def del_profile_str(self, section, keyword):
        """
        从ini配置文件中削除变量的值

        Parameters
        ----------
        section : str
            要获取的变量所在段名称
        keyword : str
            要修正的变量名称

        Raises
        ------
        IOError
            iniファイル読み込むエラー。
        """

        config = ConfigObj(self.inifile_path, encoding='UTF8')
        #  ------------------------------------------------------------------------
        #  指定キーワードで対応値を削除
        #  ------------------------------------------------------------------------
        if section in config.keys() and keyword in config[section]:
            del config[section][keyword]
            if len(config[section]) == 0:
                del config[section]
            config.write()
            return True
        else:
            print("delete ini_option[{0}] is not exist".format(keyword))
            return False
