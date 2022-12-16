# coding=utf8
import os
import maya.mel as mel
current_path = os.path.dirname(__file__)
mel_path = os.path.abspath(os.path.join(current_path,'AdvancedSkeleton5\AdvancedSkeleton5.mel'))
adv_run = mel_path.replace("\\","/")

mel.eval('source' '"{}"'';AdvancedSkeleton5'.format(adv_run))
