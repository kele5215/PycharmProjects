#  ========================================================================
#   AmiVoice     Advanced Media, Inc.
#                ----------------------------------------------------------
#                目的: 男性・女性を識別 [社内使用 ONLY]
#                ----------------------------------------------------------
#
#   Author    :  Makoto Wada
#   Module    :  GenderDetermination.py
#   Date      :  $Id: $
#   Version   :  1.3: Makoto Wada: 無音時の処理 (Divided by Zero)
#                1.2: Makoto Wada: Proccessed Length を Used Length として扱っていたのを変更
#                1.1: Makoto Wada: 随時結果が得られるように変更
#   Remarks   :
#
#                     Copyright (c) 2006 Advanced Media, Inc.
#  ========================================================================
#
#   $Log: $
#
#  ========================================================================

#  ------------------------------------------------------------------------
#  インポート
#  ------------------------------------------------------------------------
import sys

sys.path.append("lib/XCalibur.jar")

from com.mmodal.biometrics import Library, SpeakerRecognizerFactory

from com.interactivesys.xcalibur.base import Library, LineParser, InputStreamReader, FileInputStream, ObjectInputStream, \
    OutputStreamWriter, FileOutputStream, CharSetProvider
from com.interactivesys.xcalibur.tools import Library, TrsUtteranceSet, TrsUtterance

from java.lang import Integer, Float, Exception
from java.text import ParseException
from java.util import Vector, HashMap


#  ------------------------------------------------------------------------
#  認証エンジンの読み込み
#  ------------------------------------------------------------------------
def loadVerificationEngine(engine_path):
    engine_path = r"C:\work\developer\20181026-SpeakerSegregationJar\SpeakerSegregation\engine\verifier.xc.gz"
    print("LOADING VERIFICATION ENGINE:")
    verificationEngine = SpeakerRecognizerFactory.loadObject(ObjectInputStream(FileInputStream(enginePath)))
    strClasses = verificationEngine.getClasses()
    for strClass in (strClasses):
        print("\tCLASSES: ", strClass)
    print("LOADING VERIFICATION ENGINE: DONE = ", engine_path)
    print("-----------------------------------------------")
    return verificationEngine
