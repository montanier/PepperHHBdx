import jade
import numpy as np
import json

import sys
import getopt
import time

import matplotlib.pyplot as plt
from matplotlib.pyplot import ion

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.pyplot import ion
import time

bouchon_rgb = [
    [[102.31746031746032,106.45315904139433,110.12962962962963,106.88055555555556,104.1361111111111,104.1361111111111,105.11111111111111,108.60526315789474,108.08055555555555,107.97368421052632,109.85526315789474,109.905,102.63,119.64,114.8,115.82,115.13,115.13,119.2825,129.84580498866214,133.84848484848484,136.52173913043478,135.66205533596838,136.29446640316206,137.5513833992095,136.598814229249,138.61660079051384,138.02173913043478,135.80745341614906,136.18426501035196,137.19668737060042,137.57114624505928,134.21946169772258,136.54865424430642,136.3871635610766,137.00396825396825,138.4185606060606,137.5568181818182,139.125,137.1590909090909,140.8276515151515,141.11742424242425,139.42424242424244,137.2556818181818,136.93371212121212,136.32575757575756,138.6381818181818,139.1109090909091,139.93636363636364,140.16181818181818,140.63636363636363,140.39818181818183,141.12,140.2581818181818,140.17454545454547,140.86,140.74363636363637,141.46,141.46,140.99636363636364,142.69636363636363,144.2886956521739,144.03478260869565,145.1895652173913,144.73565217391305,146.7408695652174,147.17739130434782,147.96989966555185,149.06688963210703,147.8896321070234,148.12541806020067,147.88795986622074,149.72240802675586,149.37458193979933,148.1153846153846,148.07517482517483,147.23076923076923,146.94181818181818,148.04727272727274,148.5218181818182,149.20727272727274,149.09454545454545,150.36909090909091,149.3709090909091,149.32181818181817,148.9109090909091,149.19454545454545,149.08,149.1418181818182,149.8890909090909,147.8909090909091,149.7290909090909,147.9109090909091,150.07818181818183,152.20727272727274,153.78030303030303,153.64772727272728,153.27651515151516,156.67391304347825,155.36231884057972,157.1340579710145,159.39492753623188],[68.25396825396825,69.69934640522875,70.20370370370371,68.70277777777778,66.99722222222222,66.99722222222222,67.95029239766082,70.21929824561404,69.1,68.51315789473684,69.27894736842106,69.6725,65.1175,78.3,75.97631578947369,77.24,76.3025,76.3025,79.7775,89.69160997732426,93.04545454545455,94.37351778656127,94.42292490118577,94.88932806324111,95.60079051383399,94.81818181818181,96.97233201581028,96.2094861660079,94.90890269151139,95.19668737060042,96.2919254658385,96.86758893280633,95.03105590062111,96.80952380952381,96.46997929606626,97.29563492063492,97.73106060606061,97.1534090909091,98.2784090909091,97.00189393939394,99.6534090909091,99.91666666666667,98.82765151515152,97.66477272727273,97.25757575757575,97.06818181818181,98.84727272727272,99.4090909090909,99.82909090909091,100.2,100.68909090909091,100.00181818181818,100.47818181818182,100.16909090909091,100.61818181818182,101.29272727272728,100.70363636363636,101.42545454545454,101.42545454545454,101.60545454545455,103.16727272727273,104.76869565217392,104.40173913043478,104.96695652173914,104.66434782608695,106.67652173913044,106.6991304347826,107.1438127090301,108.54347826086956,107.6371237458194,108.18227424749163,107.65050167224081,108.96655518394648,109.77424749163879,109.39335664335664,109.22202797202797,108.36888111888112,108.07272727272728,108.5490909090909,109.33636363636364,109.72181818181818,109.61272727272727,111.08,110.41818181818182,109.80181818181818,109.99818181818182,110.0909090909091,110.2,110.18545454545455,110.93818181818182,109.23818181818181,110.63090909090909,109.38727272727273,110.91272727272727,112.94909090909091,114.51325757575758,114.43181818181819,113.9469696969697,116.85144927536231,116.2445652173913,117.53079710144928,119.1376811594203],[54.24603174603175,53.04357298474945,51.63756613756614,50.31388888888889,49.52777777777778,49.52777777777778,49.72222222222222,51.23099415204678,50.56111111111111,50.15,49.22631578947368,50.0625,50.415,60.72,60.20789473684211,60.5225,60.46,60.46,63.4925,71.38321995464852,74.4004329004329,75.04743083003953,75.61264822134387,76.51778656126483,76.75691699604744,77.08102766798419,78.57509881422925,78.76284584980237,77.648033126294,78.13871635610766,78.24223602484471,78.75296442687747,79.31884057971014,79.84472049689441,79.8592132505176,80.9920634920635,80.78787878787878,80.67045454545455,81.69507575757575,81.25,83.61742424242425,84.82954545454545,82.56439393939394,81.26893939393939,82.49431818181819,81.9034090909091,83.40545454545455,84.14181818181818,84.28181818181818,84.69272727272727,84.68909090909091,84.21090909090908,85.66545454545455,85.02181818181818,85.90545454545455,86.16,87.03636363636363,86.72909090909091,86.72909090909091,87.26181818181819,88.76,89.39304347826086,90.07826086956521,89.95826086956522,89.80347826086957,93.43304347826087,92.38434782608695,93.17558528428094,93.45150501672241,92.31605351170569,93.46822742474916,93.09030100334448,93.56521739130434,94.27926421404682,94.4020979020979,95.06468531468532,94.79195804195804,94.33272727272727,94.16,95.86545454545454,96.04,95.52727272727273,96.84,96.59272727272727,97.0109090909091,96.47090909090909,96.14545454545454,96.48727272727272,95.60363636363637,95.10909090909091,95.59454545454545,95.37636363636364,95.65818181818182,98.22909090909091,98.78363636363636,101.40151515151516,101.41098484848484,100.46969696969697,103.67028985507247,102.73188405797102,103.64492753623189,105.13586956521739]],
    [[144.56521739130434,144.72360248447205,148.0163043478261,149.08937198067633,149.116704805492,149.23798627002287,151.6804347826087,152.80434782608697,152.70652173913044,152.31521739130434,152.84565217391304,153.22826086956522,153.66304347826087,153.23478260869564,153.7125,155.5,155.45208333333332,154.39791666666667,154.81666666666666,156.79583333333332,155.40416666666667,158.23125,157.46041666666667,157.75208333333333,158.85416666666666,160.8875,160.8875,160.28541666666666,159.27291666666667,159.36041666666668,157.54375,158.225,157.34166666666667,157.87916666666666,157.5375,160.05,159.70833333333334,161.075,162.31666666666666,161.00416666666666,162.78968253968253,161.47420634920636,161.72222222222223,162.02579365079364,166.04166666666666,166.15719696969697,164.95454545454547,164.95454545454547,168.51136363636363,166.9034090909091,168.8598484848485,169.81060606060606,168.73295454545453,168.32007575757575,168.27272727272728,169.44886363636363,169.88636363636363,169.68560606060606,169.6439393939394,169.7310606060606,169.60795454545453,169.76325757575756,170.15719696969697,170.32954545454547,170.02272727272728,170.3655303030303,169.1193181818182,169.0340909090909,169.26136363636363,167.38636363636363,169.85227272727272,168.68371212121212,168.8068181818182,169.1818181818182,169.2651515151515],[103.42391304347827,102.66459627329192,108.95108695652173,110.2584541062802,110.1670480549199,110.13729977116705,111.67608695652174,112.66956521739131,112.56739130434782,112.28478260869565,113.02608695652174,113.56304347826087,113.8804347826087,113.86304347826086,114.9875,115.6375,115.66458333333334,115.03958333333334,115.24166666666666,116.40833333333333,115.89375,117.56666666666666,118.08125,118.14166666666667,118.325,120.15,120.15,120.45208333333333,119.37291666666667,119.20208333333333,118.19791666666667,118.9875,118.40208333333334,118.36875,117.85625,120.09583333333333,119.7,120.72083333333333,122.11875,120.975,122.23809523809524,121.92857142857143,121.92261904761905,122.4047619047619,124.39015151515152,124.95643939393939,123.9280303030303,123.9280303030303,126.46401515151516,125.51325757575758,126.50378787878788,127.23106060606061,126.70643939393939,126.62121212121212,126.58901515151516,127.62878787878788,127.50568181818181,127.2215909090909,127.12878787878788,127.03598484848484,127.0530303030303,126.89962121212122,126.9905303030303,126.96780303030303,127.38257575757575,127.11742424242425,126.66477272727273,126.60606060606061,126.78030303030303,125.87121212121212,127.4090909090909,126.66098484848484,126.41098484848484,126.37878787878788,126.48863636363636],[85.08333333333333,82.6832298136646,92.29347826086956,95.012077294686,94.64073226544622,94.51029748283753,96.66304347826087,97.55217391304348,97.95434782608696,97.09347826086956,97.71304347826087,97.36521739130434,98.3586956521739,98.9,99.95208333333333,98.56666666666666,99.95208333333333,100.00208333333333,100.64375,101.43125,101.15625,102,103.26458333333333,102.8875,103.425,104.93958333333333,104.93958333333333,104.9625,104.32916666666667,103.81875,104.30416666666666,104.43958333333333,103.525,103.56666666666666,103.2125,105.82708333333333,105.00833333333334,106.25,107.25,106.29791666666667,107.44246031746032,107.02380952380952,107.58730158730158,108.25595238095238,110.50189393939394,110.73863636363636,109.18939393939394,109.18939393939394,110.82765151515152,110.68181818181819,110.98295454545455,111.7159090909091,111.11174242424242,111.12310606060606,110.87121212121212,110.70454545454545,111.26893939393939,111.4469696969697,111.19886363636364,111.14204545454545,111.31439393939394,111.53787878787878,111.26325757575758,111.25189393939394,111.18181818181819,111.8125,111.32386363636364,110.77651515151516,111.08901515151516,110.7840909090909,110.95454545454545,110.68939393939394,111.41477272727273,111.26704545454545,110.44507575757575]],
    [[133.02910052910053,124.66071428571429,131.74812030075188,145.58035714285714,153.68350168350167,155.76599326599327,155.76599326599327,157.43602693602693,155.5731292517007,155.27891156462584,155.48979591836735,155.6768707482993,153.47108843537416,153.6904761904762,154.14795918367346,158.7646103896104,157.12012987012986,154.14285714285714,158.03401360544217,158.36201298701297,153.9591836734694,157.1530612244898,158.5952380952381,160.14455782312925,159.56972789115648,161.87337662337663,157.56006493506493,157.6672077922078,161.85227272727272,167.1289355322339,168.3193403298351,172.36231884057972,171.28695652173914,171.6855072463768,171.50972222222222,171.97916666666666,171.7159420289855,173.88055555555556,171.80289855072465,173.86816269284714,173.74166666666667,172.675,172.48055555555555,172.48055555555555,173.675,173.47083333333333,173.98611111111111,173.81944444444446,173.80416666666667,173.76805555555555,173.69354838709677,173.23001402524545,173.18934081346424,173.2608695652174,172.507713884993,172.8218793828892,172.62692847124825,172.6423562412342,172.44319775596074,172.44319775596074,172.55072463768116,173.031884057971,172.61449275362318,172.48527349228613,172.32678821879384,172.32678821879384,171.8962131837307,171.96914446002805,171.56100981767182,172.3702664796634,172.76527777777778,172.3625,173.4018817204301,172.43010752688173],[99.23544973544973,92.24107142857143,98.39285714285714,109.91428571428571,115.26599326599326,116.9006734006734,116.9006734006734,117.64814814814815,116.60374149659864,116.21598639455782,116.87244897959184,117.37925170068027,115.66326530612245,115.89965986394557,115.89625850340136,118.43181818181819,117.22077922077922,115.57312925170068,118.04251700680273,118.84902597402598,115.78911564625851,118.39965986394557,119.06122448979592,120.58673469387755,120.02891156462584,121.68668831168831,118.24350649350649,118.10551948051948,121.16071428571429,125.3808095952024,125.65067466266866,128.44202898550725,127.85797101449275,127.93188405797102,128.26805555555555,128.3736111111111,128.50434782608696,130.1263888888889,128.8,129.8555399719495,129.39166666666668,128.6513888888889,128.76805555555555,128.76805555555555,129.2,129.4111111111111,129.5222222222222,129.5625,129.62083333333334,129.4597222222222,129.66397849462365,129.5694249649369,129.88078541374475,129.3632538569425,128.7882187938289,128.92005610098175,128.9242636746143,128.8078541374474,128.92145862552596,129.1654978962132,129.3072463768116,129.59130434782608,129.27391304347827,129.4109396914446,129.19354838709677,129.19354838709677,129.15568022440394,129.0883590462833,129.18793828892007,128.6914446002805,128.925,128.65972222222223,129.5040322580645,128.997311827957],[89.26455026455027,85.14732142857143,90.11842105263158,98.03571428571429,102.78787878787878,104.02693602693603,104.02693602693603,105.25757575757575,105.27721088435374,104.33843537414965,105.71938775510205,106.01360544217687,104.78911564625851,104.15136054421768,104.60374149659864,106.06168831168831,105.34740259740259,104.6360544217687,106.19897959183673,105.97564935064935,104.92517006802721,105.93367346938776,107.10374149659864,108.30952380952381,107.86224489795919,109.47077922077922,107.50649350649351,107.64123376623377,109.89448051948052,112.32083958020989,112.6656671664168,114.21159420289855,113.74347826086957,113.24057971014493,113.21666666666667,113.73194444444445,113.84347826086956,114.22638888888889,114.14782608695653,114.84431977559608,114.14444444444445,114.16944444444445,114.09027777777777,114.09027777777777,114.28472222222223,114.45416666666667,114.48472222222222,114.59583333333333,114.21666666666667,114.93055555555556,114.97177419354838,114.8499298737728,114.4039270687237,114.62552594670407,113.96914446002805,114.08695652173913,114.52594670406732,114.1500701262272,114.00841514726508,114.51612903225806,114.37971014492754,114.25942028985507,114.3623188405797,114.3702664796634,114.11220196353436,114.11220196353436,114.34782608695652,114.22019635343618,114.01262272089761,113.6914446002805,113.74305555555556,114.72777777777777,114.54569892473118,113.24327956989248]],
    [[163.6909090909091,165.45804195804195,165.33441558441558,165.5090909090909,165.45170454545453,164.92329545454547,165.30748663101605,165.06417112299465,165.1283422459893,165.11764705882354,165.49732620320856,166.32085561497325,166.32620320855614,166.548128342246,166.4848484848485,167.68939393939394,168.7070707070707,168.16666666666666,169.01767676767676,169.04545454545453,169.3661616161616,168.760101010101,168.6338383838384,167.9949494949495,168.03535353535352,167.9520202020202,168.00757575757575,169.27777777777777,168.1489898989899,168.23737373737373,168.1489898989899,168.43686868686868,168.2020202020202,170.59661835748793,170.45652173913044,170.06763285024155,170.7246376811594,170.33091787439614,170.18686868686868,170.9671717171717,170.6010101010101,170.72222222222223,171.42822966507177,170.61483253588517,171.63397129186603,172.74641148325358,172.3062200956938,172.92583732057417,174.92105263157896,174.5287081339713,174.3062200956938,174.9306220095694,174.55263157894737,174.6267942583732,174.41626794258374,175.39473684210526,174.35406698564594,174.89952153110048,174.26315789473685,174.62200956937798,174.7846889952153,174.65071770334927,174.67224880382776,175.3181818181818,175.44258373205741,171.7070707070707,171.7020202020202,171.8422459893048,169.6898395721925,170.36631016042782,169.78877005347593,170.01069518716577,170.09358288770053,169.99197860962568],[124.69090909090909,125.47902097902097,125.07142857142857,125.7060606060606,125.32102272727273,125.28693181818181,124.18716577540107,124.2807486631016,124.00534759358288,124.17379679144385,125.33689839572193,125.41176470588235,125.29946524064171,125.59625668449198,126.48737373737374,127.64141414141415,128.2247474747475,128.4318181818182,128.10858585858585,128.07070707070707,129.02272727272728,128.5050505050505,128.61363636363637,128.17676767676767,127.87121212121212,128.6338383838384,128.57575757575756,128.90656565656565,129.04040404040404,128.81313131313132,128.80555555555554,128.36111111111111,129.06565656565655,130.16666666666666,130.29468599033817,130.03623188405797,129.56521739130434,129.80193236714976,129.71969696969697,129.43434343434345,129.24242424242425,129.48737373737373,129.94497607655504,130.0334928229665,130.63875598086125,129.91387559808612,130.3468899521531,130.51913875598086,131.45215311004785,131.55263157894737,131.77033492822966,131.92105263157896,131.97607655502392,131.79425837320574,132.10765550239233,133.32535885167465,132.98564593301435,132.5693779904306,132.24162679425837,132.0622009569378,132.1531100478469,132.27511961722487,132.17942583732057,132.36363636363637,132.08612440191388,130.95454545454547,130.510101010101,130.61764705882354,130.8101604278075,130.80213903743316,130.78342245989305,130.524064171123,130.32085561497325,130.10160427807486],[93.85454545454546,93.57692307692308,93.63636363636364,93.61212121212121,93.28977272727273,92.27556818181819,91.81016042780749,91.36363636363636,91.26737967914438,91.06951871657753,92.71122994652407,91.58823529411765,93.61764705882354,93.24866310160428,93.85606060606061,95.73484848484848,95.51767676767676,96.4419191919192,97.20454545454545,96.57575757575758,97.6969696969697,97.11868686868686,98.51515151515152,97.83585858585859,98.0050505050505,98.12373737373737,98.3030303030303,99.35353535353535,98.58080808080808,98.18434343434343,98.26515151515152,97.64141414141415,97.38383838383838,100.16183574879227,99.41062801932367,99.99033816425121,99.46618357487922,99.85507246376811,99.02777777777777,97.72222222222223,98.74242424242425,96.27020202020202,96.9401913875598,97.2535885167464,97.39712918660287,97.69856459330144,96.8133971291866,97.00478468899522,97.79665071770334,98.45933014354067,98.9090909090909,98.10765550239235,98.06459330143541,98.66985645933015,98.60287081339713,99.19856459330144,98.37320574162679,98.95454545454545,99.11483253588517,100.04545454545455,98.91387559808612,98.8157894736842,99.97607655502392,98.23205741626795,99.68899521531101,97.36111111111111,99.57575757575758,99.92245989304813,101.58021390374331,100.66577540106952,101.47326203208556,101.55882352941177,100.93048128342247,101.22459893048128]],
    [[154.7536231884058,157.00595238095238,168.41145833333334,166.3310185185185,166.41666666666666,167.92543859649123,167.79166666666666,168.32083333333333,167.4890350877193,165.16447368421052,162.88815789473685,162.54605263157896,163.51754385964912,165.34868421052633,166.44956140350877,165.70394736842104,165.70394736842104,163.9780701754386,163.40131578947367,162.4298245614035,161.66228070175438,161.5548245614035,162.3815789473684,161.5438596491228,161.28947368421052,161.1359649122807,160.61622807017545,160.359649122807,160.22149122807016,159.87280701754386,159.8421052631579,159.28070175438597,159.34649122807016,159.2982456140351,159.18859649122808,159.37280701754386,159.78947368421052,159.859649122807,159.41008771929825,159.41008771929825,158.92105263157896,159.14254385964912,159.42543859649123,159.30043859649123,159.34868421052633,159.8530701754386,159.6732456140351,160.15131578947367,159.67763157894737,160.1951754385965,160.04166666666666,160.29166666666666,160.4517543859649,160.66228070175438,160.4517543859649,160.19078947368422,159.99122807017545,159.69736842105263,159.6578947368421,160.07894736842104,159.92763157894737,159.92763157894737,159.85526315789474,159.359649122807,159.82456140350877,159.39254385964912,159.31359649122808,158.83771929824562,158.95194508009152,158.22425629290618,158.5537757437071,158.43478260869566,158.4599542334096,158.38672768878718,158.1945080091533,158.76887871853546,158.7437070938215,158.3020594965675,158.44393592677346,158.37070938215103,158.30434782608697,158.8466819221968,158.4462242562929,158.2196796338673,158.37070938215103,157.8192219679634,158.37070938215103,158.14645308924486,158.22654462242562,157.52402745995423,157.62700228832952,157.36155606407323,157.6887871853547,157.32723112128147,157.2425629290618,156.75057208237988,156.5537757437071,155.86727688787187,155.86727688787187,154.85354691075514,154.8970251716247,156.41647597254004,157.37528604118992,158.50343249427917,159.09839816933638,158.9908466819222,158.22196796338673,158.72768878718534,158.72768878718534,158.67505720823797,158.75972540045765,158.61098398169335,158.33180778032036,158.01830663615561,157.99771167048056,158.4462242562929,157.82151029748283,157.72311212814645,157.72311212814645,157.5537757437071,156.7345537757437,155.48970251716247,154.94050343249427,154.29977116704805,154.66361556064072,154.85354691075514,155.20823798627003,155.07551487414187,155.37757437070937,155.25400457665904,155.25400457665904,155.44851258581235,155.88558352402745,155.55835240274598,156.00686498855836,155.954233409611,156.837528604119,156.4828375286041,157.2745995423341,157.2288329519451,157.47826086956522,157.81235697940502,157.93821510297482,157.51487414187642,157.51487414187642,157.65903890160183,157.66132723112128,157.49427917620136,157.162471395881,156.99771167048056,156.57894736842104,156.7061403508772,157.35526315789474,157.22368421052633,156.84429824561403,156.9451754385965,156.46491228070175,156.56359649122808,155.64254385964912,155.64254385964912,155.84868421052633,155.95394736842104,155.3311403508772,154.45394736842104,154.90131578947367,155.30043859649123,155.15350877192984,155.1951754385965,155.39254385964912,154.68421052631578,154.7171052631579,154.609649122807,154.57456140350877,154.65131578947367,154.23245614035088,154.23245614035088,154.62280701754386,155.07456140350877,155.0482456140351,154.5438596491228,154.57894736842104,155.52850877192984,155.1315789473684,154.58991228070175,155.18640350877192,154.6732456140351,154.6732456140351,155.01754385964912,154.85745614035088,154.71271929824562,155.07236842105263,154.76754385964912,154.84429824561403,154.62938596491227,154.56578947368422,154.56578947368422,154.58552631578948,154.62719298245614,154.72587719298247,154.7061403508772,155.00438596491227,155.08333333333334,155.41666666666666,155.57236842105263,155.57236842105263,155.6469298245614,155.09429824561403,154.7982456140351,154.80701754385964,154.80701754385964,154.5065789473684,154.03070175438597,153.96052631578948,154.93640350877192,155.27412280701753,154.890350877193,155.57894736842104,156.13815789473685,156.13815789473685,156.49561403508773,156.53508771929825,156.7171052631579,157.07236842105263,157.43201754385964,157.17543859649123,157.2565789473684,156.9934210526316,156.4934210526316,156.4934210526316,156.76315789473685,156.6184210526316,156.11184210526315,156.25219298245614,156.31359649122808,155.4232456140351,155.4078947368421,155.2171052631579,155.10745614035088,154.8815789473684,154.8815789473684,155.0482456140351,155.640350877193,155.29605263157896,155.07236842105263,154.8048245614035,155.34868421052633,154.9078947368421,154.56578947368422,154.56578947368422],[119.23550724637681,120.8422619047619,126.66927083333333,125.77083333333333,125.10964912280701,126.10526315789474,125.8875,125.73125,125.3048245614035,124.3048245614035,123.1907894736842,122.83991228070175,123.26315789473684,124.51973684210526,125.66666666666667,125.10087719298245,125.10087719298245,123.94298245614036,123.3201754385965,122.77412280701755,122.04824561403508,122.25219298245614,121.8859649122807,122.03070175438596,121.7280701754386,121.55263157894737,121.39912280701755,121.87061403508773,121.99342105263158,121.75219298245614,121.6907894736842,121.38377192982456,121.21052631578948,121.16447368421052,121.28728070175438,121.34429824561404,121.20614035087719,121.47368421052632,121.59210526315789,121.59210526315789,121.7390350877193,121.68640350877193,122.03070175438596,121.91885964912281,121.98026315789474,121.90570175438596,121.9407894736842,121.87719298245614,121.94956140350877,121.78289473684211,122.03289473684211,121.95394736842105,122.15350877192982,122.16008771929825,122.29824561403508,122.41228070175438,122.58991228070175,122.39912280701755,122.17763157894737,121.93201754385964,121.57236842105263,121.57236842105263,121.56798245614036,121.73464912280701,121.33771929824562,121.68201754385964,121.4451754385965,121.34210526315789,121.34096109839817,121.34096109839817,121.08466819221968,121.24027459954233,120.95652173913044,120.73913043478261,120.62013729977117,120.75514874141876,120.7299771167048,120.98398169336384,120.71395881006865,120.60183066361556,120.89016018306636,120.94736842105263,121.11441647597255,121.33638443935926,121.6086956521739,121.69107551487414,120.92677345537757,120.85354691075514,120.62013729977117,120.07322654462243,119.51716247139588,119.40503432494279,119.61327231121281,119.66361556064074,119.57437070938215,119.46453089244851,118.86498855835241,118.55606407322655,118.55606407322655,117.24713958810068,116.558352402746,118.06178489702518,119.83752860411899,120.81922196796339,121.01372997711671,121.78489702517163,121.86727688787185,121.62700228832952,121.62700228832952,121.75286041189932,121.64530892448512,121.49427917620137,121.07093821510297,120.31807780320366,120.48512585812357,120.61784897025171,120.58810068649886,120.50572082379863,120.50572082379863,120.16933638443936,119.59725400457666,118.24485125858124,117.39816933638444,116.49885583524028,117.11441647597255,117.17620137299771,117.15789473684211,117.39816933638444,117.16475972540046,117.39359267734554,117.39359267734554,117.46453089244851,117.48970251716247,117.8787185354691,118.09839816933638,118.93363844393593,119.04347826086956,119.57437070938215,119.62929061784897,120.02059496567506,120.08924485125858,120.05263157894737,120.11670480549199,120.07093821510297,120.07093821510297,120.16247139588101,119.99313501144165,119.92906178489703,119.67276887871853,119.54919908466819,119.21052631578948,119.25,119.05263157894737,118.73245614035088,118.8048245614035,118.78728070175438,118.78289473684211,118.09868421052632,118.08991228070175,118.08991228070175,117.96491228070175,117.40131578947368,117.13157894736842,117.32456140350877,116.2609649122807,116.10964912280701,116.19736842105263,116.28947368421052,116.00438596491227,116.21052631578948,116.14912280701755,115.98245614035088,116.2719298245614,116.09649122807018,116.65570175438596,116.65570175438596,116.08552631578948,115.99780701754386,115.99342105263158,116.3530701754386,116.25657894736842,115.96710526315789,116.61184210526316,116.65131578947368,116.63377192982456,116.75877192982456,116.75877192982456,116.72149122807018,116.58991228070175,116.67763157894737,116.30043859649123,116.20175438596492,116.59868421052632,116.25657894736842,116.21929824561404,116.21929824561404,116.42324561403508,116.64473684210526,116.35745614035088,116.66885964912281,117.29385964912281,117.3859649122807,117.18640350877193,117.12061403508773,117.12061403508773,116.89912280701755,116.76315789473684,116.83991228070175,116.56140350877193,116.56140350877193,116.63815789473684,116.43859649122807,116.77631578947368,117.05043859649123,117.16228070175438,117.54824561403508,117.79824561403508,118.43859649122807,118.43859649122807,118.86184210526316,119.40131578947368,119.54385964912281,119.71271929824562,119.87280701754386,120.22368421052632,120.22587719298245,120.26315789473684,120.35964912280701,120.35964912280701,119.83771929824562,118.96491228070175,119.05043859649123,118.19956140350877,117.90131578947368,117.90131578947368,117.65131578947368,117.58991228070175,117.63157894736842,117.6469298245614,117.6469298245614,117.4890350877193,117.63377192982456,117.21929824561404,116.73684210526316,116.98245614035088,116.3157894736842,116.62938596491227,116.56359649122807,116.56359649122807],[112.40942028985508,113.54464285714286,115.0859375,113.61805555555556,112.2280701754386,113.67324561403508,113.51458333333333,114.43541666666667,114.41666666666667,112.69736842105263,112.64473684210526,111.8859649122807,112.17543859649123,113.05701754385964,114.20175438596492,113.61184210526316,113.61184210526316,112.91447368421052,112.13377192982456,112.05701754385964,112.41447368421052,112.26754385964912,111.8048245614035,111.95394736842105,111.57894736842105,111.98684210526316,110.44956140350877,111.46052631578948,111.03947368421052,110.95394736842105,110.71491228070175,110.64254385964912,110.9342105263158,110.89912280701755,110.8157894736842,111.00438596491227,111.11184210526316,111.26973684210526,111.53508771929825,111.53508771929825,111.1842105263158,111.88815789473684,111.16447368421052,110.9451754385965,111.31359649122807,111.2719298245614,111.48464912280701,111.61184210526316,111.72587719298245,111.32675438596492,111.46271929824562,111.18859649122807,111.12061403508773,111.5,111.81359649122807,111.34868421052632,111.24561403508773,111.73026315789474,111.71929824561404,111.36842105263158,111.46052631578948,111.46052631578948,111.15570175438596,111.02850877192982,112.01315789473684,110.9890350877193,111.1798245614035,111.51973684210526,110.60640732265446,110.72082379862701,110.84210526315789,110.02745995423341,110.05720823798627,110.78489702517163,111.11441647597255,110.57437070938215,110.91075514874142,110.94736842105263,110.62700228832952,111.1533180778032,111.19679633867277,110.74370709382151,111.51716247139588,111.2837528604119,110.86498855835241,111.37528604118994,111.20823798627002,111.23340961098398,111.1716247139588,109.92448512585813,109.69794050343249,109.53089244851259,109.54462242562929,109.66132723112128,109.09153318077803,109.2883295194508,108.90160183066362,107.65217391304348,107.65217391304348,106.53318077803203,105.3157894736842,106.6086956521739,109.62013729977117,110.89473684210526,110.90846681922197,111.2745995423341,111.61784897025171,112.1441647597254,112.1441647597254,111.91304347826087,112.2654462242563,110.76430205949657,109.88329519450801,110.19221967963387,110.08009153318078,110.37528604118994,110.61784897025171,109.92448512585813,109.92448512585813,109.54233409610984,108.7025171624714,107.7025171624714,105.76659038901602,104.78718535469108,105.47597254004576,105.46910755148741,106.51258581235697,107.31807780320366,106.36842105263158,107.03890160183066,107.03890160183066,106.55377574370709,107.66132723112128,106.91762013729978,107.95194508009153,108.04576659038902,108.52173913043478,108.52860411899313,110.24485125858124,110.00915331807781,110.79405034324942,110.21281464530892,109.7116704805492,110.46224256292906,110.46224256292906,110.15102974828375,110.44851258581235,110.64073226544622,109.95423340961098,109.7254004576659,109.16475972540046,109.10964912280701,108.95394736842105,109.45394736842105,109.32894736842105,108.26973684210526,108.23464912280701,107.46710526315789,107.94956140350877,107.94956140350877,107.83114035087719,107.00438596491227,106.46052631578948,105.77631578947368,105.1907894736842,105.66447368421052,105.42543859649123,105.21929824561404,105.68201754385964,105.35087719298245,104.80263157894737,105.35526315789474,104.96491228070175,105.87280701754386,105.17324561403508,105.17324561403508,105.31798245614036,105.03508771929825,105.70614035087719,104.73245614035088,106.19736842105263,105.91228070175438,105.35087719298245,105.22368421052632,105.60745614035088,105.50657894736842,105.50657894736842,105.73026315789474,106.83552631578948,105.23026315789474,105.58552631578948,106.2280701754386,104.5592105263158,105.98464912280701,105.31798245614036,105.31798245614036,105.63815789473684,105.34429824561404,105.57675438596492,105.9298245614035,106.26315789473684,106.02850877192982,106.33333333333333,106.54166666666667,106.54166666666667,106.0701754385965,105.90570175438596,106.08114035087719,105.32456140350877,105.32456140350877,105.17324561403508,105.82456140350877,105.5592105263158,105.77412280701755,106.5657894736842,106.53070175438596,107.33991228070175,108.3092105263158,108.3092105263158,108.90789473684211,108.60745614035088,109.75877192982456,109.42543859649123,110.24122807017544,110.1469298245614,110.44736842105263,110.15131578947368,109.88815789473684,109.88815789473684,109.52850877192982,109.3092105263158,108.65131578947368,108.28508771929825,107.70394736842105,107.68640350877193,107.0548245614035,106.90570175438596,107.12061403508773,107.17763157894737,107.17763157894737,106.32894736842105,106.49780701754386,106.91447368421052,106.3530701754386,105.71710526315789,106.26754385964912,105.7390350877193,106.29166666666667,106.29166666666667]]
]

dataArray = []
dataHistory = []
timeArray = []

dateDebut = time.time ()

def main():

        start_time = time.time()
        ion()
        fig = plt.figure()
        plt.axis([0, 10, 0, 100])
        fig.suptitle("Cardio-frequency")
        subplt = fig.add_subplot(1, 1, 1)
        line1, = subplt.plot([], [], 'r-')
        buffer_window = 230

        freq_record = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        time_record = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        while True:
            for i in range(0, len(bouchon_rgb)) :
                fftresult = parse_RGB(len(bouchon_rgb[i][0]), bouchon_rgb[i])
                freq = frequencyExtract(fftresult, 15)
                freq_record.append(freq)
                dataHistory.append(freq_record.pop(0))
                line1.set_ydata(freq_record)
                line1.set_xdata(time_record)
                fig.canvas.draw()
                plt.pause(0.01)

def parse_RGB(buffer_window, sample):
        X = np.ndarray(shape = (3, buffer_window), buffer= np.array(sample))
        X = normalize_matrix(X)
        ICA = jade.main(X)
        signalFFT = parse_ICA_results(ICA)
        return signalFFT

def parse_ICA_results(ICA):

        red = np.squeeze(np.asarray(ICA[:, 0])).tolist()
        green = np.squeeze(np.asarray(ICA[:, 1])).tolist()
        blue = np.squeeze(np.asarray(ICA[:, 2])).tolist()
        
        red = (np.hamming(len(red)) * red)
        green = (np.hamming(len(green)) * green)
        blue = (np.hamming(len(blue)) * blue)

        red = np.absolute(np.square(np.fft.irfft(red))).astype(float).tolist()
        green = np.absolute(np.square(np.fft.irfft(green))).astype(float).tolist()
        blue = np.absolute(np.square(np.fft.irfft(blue))).astype(float).tolist()

        power_ratio = [0, 0, 0]
        power_ratio[0] = np.sum(red)/np.amax(red)
        power_ratio[1] = np.sum(green)/np.amax(green)
        power_ratio[2] = np.sum(blue)/np.amax(blue)

        if np.argmax(power_ratio) == 0:
                signals = red
        elif np.argmax(power_ratio) == 1:
                signals = green
        else:
                signals = blue

        return signals

def normalize_matrix(matrix):

        for array in matrix:
                average_of_array = np.mean(array)
                std_dev = np.std(array)

                for i in range(len(array)):
                        array[i] = ((array[i] - average_of_array)/std_dev)
        return matrix

def normalize_array(array):

        average_of_array = np.mean(array)
        std_dev = np.std(array)

        for i in range(len(array)):
                array[i] = ((array[i] - average_of_array)/std_dev)
        return array

def frequencyExtract(fftArray, framerate):
        
        p2 = []
        freqs = []

        lenFftArray = len(fftArray)
        reverseFrame = 1.0/framerate

        frameRate = 1.0/(lenFftArray * reverseFrame)
        medium = ((lenFftArray - 1)/2 + 1) >> 0

        for i in range(medium):
            freqs.append(i * frameRate)

        for i in xrange(-(lenFftArray/2) >> 0, 0):
            p2.append(i * frameRate)

        freqs.append(p2)

        return filterFreq(fftArray, freqs, framerate)

def filterFreq(fftArray, freqs, framerate) :
    
    normalizedFreqs = []
    filteredFreqBin = []

    freqObj = zip(freqs, fftArray)

    for i in range(len(freqObj)) :
        freq = freqObj[i][0]
        if ((freq > 0.80) and (freq < 3)) :
            normalizedFreqs.append(abs(freqObj[i][1])**2)
            filteredFreqBin.append((freq)/1)
    
    idx = np.argmax(np.asarray(normalizedFreqs))
    freq_in_hertz = filteredFreqBin[idx]
    
    return freq_in_hertz * 60

def animate(i):
   xar = []
   yar = []
   for j in range(len(dataArray)):
        xar.append(j)
        yar.append(dataArray[j])
   ax1.clear()
   ax1.plot(xar,yar)


if __name__ == "__main__":
    sys.exit(main())
