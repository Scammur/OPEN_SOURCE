#=======><IMPORT_BOX><========#
import random
from random import randint
from string import *
try:
     import os, storage, requests, mechanize, bs4, futures
except ImportError:
    os.system('clear')


#=======><COLOR><========#
T="\033[1;31m"            # Red
A="\033[1;32m"         # Green
R="\033[1;33m"        # Yellow
RT="\033[1;37m"         # White

#=======><RANDOM_CHOICE_COLOR><========#
color = [T,A,R,RT]
CENT_PH = random.choice(color)
#owner created (cent)
#=======><MODEL'S><========#
Oppo = """
CPH1869
CPH1929
CPH2107
CPH2238
CPH2389
CPH2401
CPH2407
CPH2413
CPH2415
CPH241
CPH2419
CPH2455
CPH2459
CPH2461
CPH2471
CPH2473
CPH2477
CPH8893
CPH2321
CPH2341
CPH2373
CPH2083
CPH2071
CPH2077
CPH2185
CPH2179
CPH2269
CPH2421
CPH2349
CPH2271
CPH1923
CPH1925
CPH1837
CPH2015
CPH2073
CPH2081
CPH2029
CPH2031
CPH2137
CPH1605
CPH1803
CPH1853
CPH1805
CPH1809
CPH1851
CPH1931
CPH1959
CPH1933
CPH1935
CPH1943
CPH2061
CPH2069
CPH2127
CPH2131
CPH2139
CPH2135
CPH2239
CPH2195
CPH2273
CPH2325
CPH2309
CPH1701
CPH2387
CPH1909
CPH1920
CPH1912
CPH1901
CPH1903
CPH1905
CPH1717
CPH1801
CPH2067
CPH2099
CPH2161
CPH2219
CPH2197
CPH2263
CPH2375
CPH2339
CPH1715
CPH2385
CPH1729
CPH1827
CPH1938
CPH1937
CPH1939
CPH1941
CPH2001
CPH2021
CPH2059
CPH2121
CPH2123
CPH2203
CPH2333
CPH2365
CPH1913
CPH1911
CPH1915
CPH1969
CPH2209
CPH1987
CPH2095
CPH2119
CPH2285
CPH2213
CPH2223
CPH2363
CPH1609
CPH1613
CPH1723
CPH1727
CPH1725
CPH1819
CPH1821
CPH1825
CPH1881
CPH1823
CPH1871
CPH1875
CPH2023
CPH2005
CPH2025
CPH2207
CPH2173
CPH2307
CPH2305
CPH2337
CPH1955
CPH1707
CPH1719
CPH1721
CPH1835
CPH1831
CPH1833
CPH1879
CPH1893
CPH1877
CPH1607
CPH1611
CPH1917
CPH1919
CPH1907
CPH1989
CPH1945
CPH1951
CPH2043
CPH2035
CPH2037
CPH2036
CPH2009
CPH2013
CPH2113
CPH2091
CPH2125
CPH2109
CPH2089
CPH2065
CPH2159
CPH2145
CPH2205
CPH2201
CPH2199
CPH2217
CPH1921
CPH2211
CPH2235
CPH2251
CPH2249
CPH2247
CPH2237
CPH2371
CPH2293
CPH2353
CPH2343
CPH2359
CPH2357
CPH2457
CPH1983
CPH1979
CPH2451
CPH2419
CPH2389
CPH2351
CPH2332
CPH2331
CPH2261
CPH2238
CPH2107
CPH2048
CPH1929
CPH1985
CPH1869
CPH1615
CPH1664
CPH1451
CPH1235
CPH1114
""".splitlines()

galaxy = random.choice(Oppo)

#=======><RANDOM_STRING><========#
fblc = random.choice(["th_TH","en_GB","en_US","fr_FR", "en_US", "es_ES", "de_DE", "it_IT", "ru_RU", "zh_CN", "ja_JP"])
fbpn = random.choice(["com.facebook.katana","com.facebook.lite"])
rt = random.choice(["FB4A","EMA"])
fbcr = random.choice(["AIS','cricket","MegaFon","Viettel Telecom","TRUE-H","TM","GLOBE","null","VIETTEL","TELCEL","O2-CZ","U.S. Cellular","SUN","TelkomSA","Verizon","Plus","Claro BR","T-Mobile","airtel","PLAY (T-Mobile)","VIVACOM","lifecell","Yoigo","life:) BY","vodafone.de","Vodafone","PosteMobile","Verizon Wireless","Movistar","HOME","SAZKAmobilCZ","Astelit-LIFE;FBMF","AT&amp;amp-T","Grameenphone","Robi","Banglalink","Willkommen"])

phone = random.choice(["Oppo"])
fbca = random.choice(["armeabi-v7a:armeabi","arm64-v8a:"])

#=======><UA><========#
CENT = f"{CENT_PH}[FBAN/"+str(rt)+";FBAV/"+str(random.randint(111,458))+".0.0."+str(random.randrange(11,99))+"."+str(random.randint(45,455))+";FBPN/"+str(fbpn)+";FBLC/"+str(fblc)+";FBBV/"+str(random.randint(111111111,999999999))+";FBCR/"+str(fbcr)+";FBMF/"+str(phone)+";FBBD/"+str(phone)+";FBDV/"+str(galaxy)+";FBSV/"+str(random.randint(6,14))+";FBCA/"+str(fbca)+";FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
print(f"UA- {CENT}")
print(f"\033[97;1m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
