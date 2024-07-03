import json
import os

import requests
from django.http import JsonResponse
from .models import College


def bulk_insert_colleges(data):
    colleges = [College(**item) for item in data]
    College.objects.bulk_create(colleges)


def get_college_list(request):
    try:
        colleges = College.objects.values()
        data = list(colleges)
        return JsonResponse({'code': 200, 'msg': 'success', 'data': data})
    except Exception as e:
        return JsonResponse({'msg': 'An error occurred: {}'.format(e)})



def get_college_logo(request, filename):
    return None

def crawl_college_logo():
    url = 'https://www.shanghairanking.cn/_nuxt/static/1718865654/rankings/bcur/202411/payload.js'
    r = requests.get(url, timeout=20)
    if r.status_code == 200:
        r.encoding = 'utf-8'
        content = r.text
        while content.find('univUp:"') != -1:
            # 切出校徽地址
            content = content[content.find('univLogo:"') + 10:]
            collegeLogo = content[:content.find('"')]
            Logo_name = collegeLogo[collegeLogo.find('u002F') + 5:]
            photo_url = 'https://www.shanghairanking.cn/_uni/' + collegeLogo[:collegeLogo.find('u002F')] + Logo_name
            logo = requests.get(photo_url)
            try:
                with open(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + Logo_name,
                          'wb') as f:
                    f.write(logo.content)
            except Exception as e:
                pass


def crawl_college_data(request):
    url = 'https://www.shanghairanking.cn/_nuxt/static/1718865654/rankings/bcur/202411/payload.js'
    r = requests.get(url, timeout=20)
    a_ = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
        'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
        'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z', '_', '$', 'aa', 'ab', 'ac', 'ad', 'ae', 'af', 'ag', 'ah',
        'ai', 'aj', 'ak', 'al', 'am', 'an', 'ao', 'ap', 'aq', 'ar', 'as', 'at', 'au',
        'av', 'aw', 'ax', 'ay', 'az', 'aA', 'aB', 'aC', 'aD', 'aE', 'aF', 'aG', 'aH',
        'aI', 'aJ', 'aK', 'aL', 'aM', 'aN', 'aO', 'aP', 'aQ', 'aR', 'aS', 'aT', 'aU',
        'aV', 'aW', 'aX', 'aY', 'aZ', 'a_', 'a$', 'ba', 'bb', 'bc', 'bd', 'be', 'bf',
        'bg', 'bh', 'bi', 'bj', 'bk', 'bl', 'bm', 'bn', 'bo', 'bp', 'bq', 'br', 'bs',
        'bt', 'bu', 'bv', 'bw', 'bx', 'by', 'bz', 'bA', 'bB', 'bC', 'bD', 'bE', 'bF',
        'bG', 'bH', 'bI', 'bJ', 'bK', 'bL', 'bM', 'bN', 'bO', 'bP', 'bQ', 'bR', 'bS',
        'bT', 'bU', 'bV', 'bW', 'bX', 'bY', 'bZ', 'b_', 'b$', 'ca', 'cb', 'cc', 'cd',
        'ce', 'cf', 'cg', 'ch', 'ci', 'cj', 'ck', 'cl', 'cm', 'cn', 'co', 'cp', 'cq',
        'cr', 'cs', 'ct', 'cu', 'cv', 'cw', 'cx', 'cy', 'cz', 'cA', 'cB', 'cC', 'cD',
        'cE', 'cF', 'cG', 'cH', 'cI', 'cJ', 'cK', 'cL', 'cM', 'cN', 'cO', 'cP', 'cQ',
        'cR', 'cS', 'cT', 'cU', 'cV', 'cW', 'cX', 'cY', 'cZ', 'c_', 'c$', 'da', 'db',
        'dc', 'dd', 'de', 'df', 'dg', 'dh', 'di', 'dj', 'dk', 'dl', 'dm', 'dn', 'do0',
        'dp', 'dq', 'dr', 'ds', 'dt', 'du', 'dv', 'dw', 'dx', 'dy', 'dz', 'dA', 'dB',
        'dC', 'dD', 'dE', 'dF', 'dG', 'dH', 'dI', 'dJ', 'dK', 'dL', 'dM', 'dN', 'dO',
        'dP', 'dQ', 'dR', 'dS', 'dT', 'dU', 'dV', 'dW', 'dX', 'dY', 'dZ', 'd_', 'd$',
        'ea', 'eb', 'ec', 'ed', 'ee', 'ef', 'eg', 'eh', 'ei', 'ej', 'ek', 'el', 'em',
        'en', 'eo', 'ep', 'eq', 'er', 'es', 'et', 'eu', 'ev', 'ew', 'ex', 'ey', 'ez',
        'eA', 'eB', 'eC', 'eD', 'eE', 'eF', 'eG', 'eH', 'eI', 'eJ', 'eK', 'eL', 'eM',
        'eN', 'eO', 'eP', 'eQ', 'eR', 'eS', 'eT', 'eU', 'eV', 'eW', 'eX', 'eY', 'eZ',
        'e_', 'e$', 'fa', 'fb', 'fc', 'fd', 'fe', 'ff', 'fg', 'fh', 'fi', 'fj', 'fk',
        'fl', 'fm', 'fn', 'fo', 'fp', 'fq', 'fr', 'fs', 'ft', 'fu', 'fv', 'fw', 'fx',
        'fy', 'fz', 'fA', 'fB', 'fC', 'fD', 'fE', 'fF', 'fG', 'fH', 'fI', 'fJ', 'fK',
        'fL', 'fM', 'fN', 'fO', 'fP', 'fQ', 'fR', 'fS', 'fT', 'fU', 'fV', 'fW', 'fX',
        'fY', 'fZ', 'f_', 'f$', 'ga', 'gb', 'gc', 'gd', 'ge', 'gf', 'gg', 'gh', 'gi',
        'gj', 'gk', 'gl', 'gm', 'gn', 'go', 'gp', 'gq', 'gr', 'gs', 'gt', 'gu', 'gv',
        'gw', 'gx', 'gy', 'gz', 'gA', 'gB', 'gC', 'gD', 'gE', 'gF', 'gG', 'gH', 'gI',
        'gJ', 'gK', 'gL', 'gM', 'gN', 'gO', 'gP', 'gQ', 'gR', 'gS', 'gT', 'gU', 'gV',
        'gW', 'gX', 'gY', 'gZ', 'g_', 'g$', 'ha', 'hb', 'hc', 'hd', 'he', 'hf', 'hg',
        'hh', 'hi', 'hj', 'hk', 'hl', 'hm', 'hn', 'ho', 'hp', 'hq', 'hr', 'hs', 'ht',
        'hu', 'hv', 'hw', 'hx', 'hy', 'hz', 'hA', 'hB', 'hC', 'hD', 'hE', 'hF', 'hG',
        'hH', 'hI', 'hJ', 'hK', 'hL', 'hM', 'hN', 'hO', 'hP', 'hQ', 'hR', 'hS', 'hT',
        'hU', 'hV', 'hW', 'hX', 'hY', 'hZ', 'h_', 'h$', 'ia', 'ib', 'ic', 'id', 'ie',
        'if0', 'ig', 'ih', 'ii', 'ij', 'ik', 'il', 'im', 'in0', 'io', 'ip', 'iq', 'ir',
        'is', 'it', 'iu', 'iv', 'iw', 'ix', 'iy', 'iz', 'iA', 'iB', 'iC', 'iD', 'iE',
        'iF', 'iG', 'iH', 'iI', 'iJ', 'iK', 'iL', 'iM', 'iN', 'iO', 'iP', 'iQ', 'iR',
        'iS', 'iT', 'iU', 'iV', 'iW', 'iX', 'iY', 'iZ', 'i_', 'i$', 'ja', 'jb', 'jc',
        'jd', 'je', 'jf', 'jg', 'jh', 'ji', 'jj', 'jk', 'jl', 'jm', 'jn', 'jo', 'jp',
        'jq', 'jr', 'js', 'jt', 'ju', 'jv', 'jw', 'jx', 'jy', 'jz', 'jA', 'jB', 'jC',
        'jD', 'jE', 'jF', 'jG', 'jH', 'jI', 'jJ', 'jK', 'jL', 'jM', 'jN', 'jO', 'jP', 'jQ', 'jR', 'jS',
        'jT', 'jU', 'jV', 'jW', 'jX', 'jY', 'jZ', 'j_', 'j$', 'ka', 'kb', 'kc', 'kd', 'ke', 'kf', 'kg',
        'kh', 'ki', 'kj', 'kk', 'kl', 'km', 'kn', 'ko', 'kp', 'kq', 'kr', 'ks', 'kt', 'ku', 'kv', 'kw',
        'kx', 'ky', 'kz', 'kA', 'kB', 'kC', 'kD', 'kE', 'kF', 'kG', 'kH', 'kI', 'kJ', 'kK', 'kL', 'kM',
        'kN', 'kO', 'kP', 'kQ', 'kR', 'kS', 'kT', 'kU', 'kV', 'kW', 'kX', 'kY', 'kZ', 'k_', 'k$', 'la',
        'lb', 'lc', 'ld', 'le', 'lf', 'lg', 'lh', 'li', 'lj', 'lk', 'll', 'lm', 'ln', 'lo', 'lp', 'lq',
        'lr', 'ls', 'lt', 'lu', 'lv', 'lw', 'lx', 'ly', 'lz', 'lA', 'lB', 'lC', 'lD', 'lE', 'lF', 'lG',
        'lH', 'lI', 'lJ', 'lK', 'lL', 'lM', 'lN', 'lO', 'lP', 'lQ', 'lR', 'lS', 'lT', 'lU', 'lV', 'lW',
        'lX', 'lY', 'lZ', 'l_', 'l$', 'ma', 'mb', 'mc', 'md', 'me', 'mf', 'mg', 'mh', 'mi', 'mj', 'mk',
        'ml', 'mm', 'mn', 'mo', 'mp', 'mq', 'mr', 'ms', 'mt', 'mu', 'mv', 'mw', 'mx', 'my', 'mz', 'mA',
        'mB', 'mC', 'mD', 'mE', 'mF', 'mG', 'mH', 'mI', 'mJ', 'mK', 'mL', 'mM', 'mN', 'mO', 'mP', 'mQ',
        'mR', 'mS', 'mT', 'mU', 'mV', 'mW', 'mX', 'mY', 'mZ', 'm_', 'm$', 'na', 'nb', 'nc', 'nd', 'ne',
        'nf', 'ng', 'nh', 'ni', 'nj', 'nk', 'nl', 'nm', 'nn', 'no', 'np', 'nq', 'nr', 'ns', 'nt', 'nu',
        'nv', 'nw', 'nx', 'ny', 'nz', 'nA', 'nB', 'nC', 'nD', 'nE', 'nF', 'nG', 'nH', 'nI', 'nJ', 'nK',
        'nL', 'nM', 'nN', 'nO', 'nP', 'nQ', 'nR', 'nS', 'nT', 'nU', 'nV', 'nW', 'nX', 'nY', 'nZ', 'n_',
        'n$', 'oa', 'ob', 'oc', 'od', 'oe', 'of', 'og', 'oh', 'oi', 'oj', 'ok', 'ol', 'om', 'on', 'oo',
        'op', 'oq', 'or', 'os', 'ot', 'ou', 'ov', 'ow', 'ox', 'oy', 'oz', 'oA', 'oB', 'oC', 'oD', 'oE',
        'oF', 'oG', 'oH', 'oI', 'oJ', 'oK', 'oL', 'oM', 'oN', 'oO', 'oP', 'oQ', 'oR', 'oS', 'oT', 'oU',
        'oV', 'oW', 'oX', 'oY', 'oZ', 'o_', 'o$', 'pa', 'pb', 'pc', 'pd', 'pe', 'pf', 'pg', 'ph', 'pi',
        'pj', 'pk', 'pl', 'pm', 'pn', 'po', 'pp', 'pq', 'pr', 'ps', 'pt', 'pu', 'pv', 'pw', 'px', 'py',
        'pz', 'pA', 'pB', 'pC', 'pD', 'pE', 'pF', 'pG', 'pH', 'pI', 'pJ', 'pK', 'pL', 'pM', 'pN', 'pO',
        'pP', 'pQ', 'pR', 'pS'
    ]

    b_ = ["", "false", "null", 0, "理工", "综合", "true", "师范", "双一流", "211", "江苏", "985", "农业", "山东",
          "河北",
          "河南", "北京", "辽宁", "陕西", "四川", "广东", "湖北", "湖南", "浙江", "安徽", "江西", "山西", "黑龙江",
          "吉林",
          "上海", "福建", "广西", "云南", "贵州", "甘肃", 2, "重庆", "内蒙古", "天津", "新疆", 1,
          "2023-01-05T00:00:00+08:00", "2024,2023,2022,2021,2020", "林业", "443", "17.7", "10.0", "10.1", "6.4", "5.5",
          "海南", "9.2", "9.6", "17.5", "8.4", "11.4", "9.3", "6.2", "\u003C1.0", "179", "219", "328", "336", "386",
          "389",
          "393", "402", "465", "485", "501", "12.1", "15.6", "32.6", "10.4", "10.8", "16.5", "4.8", "12.6", "5.0",
          "18.1",
          "18.7", "7.8", "14.6", "6.3", "5.4", "7.7", "3.6", "538", "540", 2024, 11, 14, 10, 15, "2024,2023", "宁夏",
          "青海", "西藏", "21.2", "28.4", "29.7", "26.9", "15.1", "12.2", "28.6", "11.7", "33.1", "23.4", "31.8",
          "11.9",
          "24.5", "16.0", "5.9", "30.6", "13.6", "20.7", "18.2", "18.6", "28.1", "9.1", "4.9", "8.1", "44.7", "31.6",
          "6.1",
          "29.5", "14.2", "6.0", "5.3", "8.3", "52", "4.4", "12.0", "5.8", "4.1", "95", "105", "126", "136", "139",
          "177",
          "186", "192", "196", "206", "239", "243", "249", "267", "274", "283", "295", "305", "310", "315", "317",
          "321",
          "331", "334", "342", "344", "347", "350", "356", "365", "373", "376", "396", "399", "406", "409", "413",
          "415",
          "424", "428", "430", "432", "441", 110.1, "447", "449", "456", "468", "477", "488", "499", "505", "507",
          "512",
          "514", "517", "520", "526", "529", "536", "553", "558", "570", "589", 7, "30.5", "26.4", "12.8", "29.2",
          "29.0",
          "50.4", "21.9", "38.9", "25.8", "9.9", "14.9", "30.4", "20.8", "50.2", "40.2", "14.3", "27.5", "30.0", "29.3",
          "22.6", "15.7", "19.9", "24.2", "38.4", "31.3", "12.5", "30.2", "10.6", "4.2", "9.8", "20.5", "30.8", "12.7",
          "13.8", "10.5", "38.7", "16.2", "4.5", "23.8", "6.8", "8.0", "42.4", "1.6", "8.5", "13.4", "2.9", "27.4",
          "3.9",
          "39.4", "3.3", "6.5", "13.5", "3.8", 186.8, 166.8, 132, 130.8, 118.5, 118, 117.5, 116.8, 106.9, 103, 100.1,
          "537",
          "542", "543", "544", "545", 4, 13, "中国大学排名（主榜）", 25, 16, 17, "全部", "1", "36.1", "50.0", 5, "2",
          "34.9",
          "52.8", 3, "3", 6, "4", "62.3", "39.6", "5", "21.3", "51.0", "6", "7", "13.3", "50.7", "11.2", "44.2", "8",
          "32.2", "43.6", "49.7", "9", "31.7", "38.6", "44.3", "10", "34.6", "28.7", "11", "40.6", "12", "48.2", "53.5",
          "14.1", "13", "44.5", "22.1", "14", "23.6", "47.1", "15", "49.1", "28.3", "16", "37.9", "18.8", "33.5",
          "20.4",
          "17", "35.2", "18", "39.5", "42.7", "12.9", "19", "32.1", "46.4", "29.8", "20", "31.9", "26.1", "25.2", "21",
          "33.3", "7.9", "22", "19.2", "23", "33.4", "25.5", "25.9", "24", "28.0", "25", "33.7", "27.1", "26", "27",
          "41.6",
          "36.2", "28", "48.0", "17.1", "29", "40.3", "30", "19.1", "31", "32", "45.6", "27.7", "33", "7.3", "17.2",
          "34",
          "24.4", "35", "22.9", "45.7", "8.6", "19.5", "36", "12.3", "37", "38", "9.4", "39", "21.1", "28.9", "40",
          "7.1",
          "27.3", "9.5", "41", "11.6", "9.0", "42", "145.6", "18.4", "43", "21.4", "44", "30.9", "20.6", "45", "41.3",
          "46",
          "47", "6.6", "43.9", "6.7", "48", "49", "5.7", "7.0", "50", "5.2", "51", "16.4", "15.2", 322.7, "43.3", "6.9",
          "54", "15.0", "14.4", "55", "141.3", "56", "44.9", "140.1", "8.8", "57", "2.0", "58", "59", "11.1", "60",
          "16.7",
          "40.1", "61", "62", "63", "16.8", "41.5", "64", "65", "4.6", "11.3", "66", "67", "2.4", "68", "69", "24.8",
          "70",
          "2.6", "71", "72", "73", "74", "13.9", "25.0", "75", "76", "4.3", "77", "3.1", "78", "79", "80", "27.2", "81",
          "15.8", "1.9", "82", "26.6", "5.1", "83", "19.6", "84", "85", "39.2", "86", "1.2", "87", "88", "89", "90",
          "37.0",
          "91", "4.7", "92", "93", "94", 249.5, "17.6", "97", "98", "99", "100", "101", "102", "103", "104", 245.4,
          "107",
          "108", "109", "110", "111", "112", "113", "114", "115", "116", "117", "118", "119", "120", "121", "122",
          "123",
          "124", "125", 217.7, "128", "129", "130", "131", "132", "133", "134", "135", 209.4, "138", 206.9, "141",
          "142",
          "143", "144", "145", "146", "147", "148", "149", "150", "151", "152", "153", "154", "155", "156", "157",
          "158",
          "159", "160", "161", "162", "163", "164", "165", "166", "167", "168", "169", "170", "171", "172", "173",
          "174",
          "175", "176", 187.1, "182", "183", "184", "185", 182.1, "188", "189", "190", "191", 179.3, "194", "195",
          177.2,
          "198", "199", "200", "201", "202", "203", "204", "205", 173.3, "208", "209", "210", 170.4, "213", "214",
          "215",
          "216", "217", "218", "222", "223", "224", "225", "226", "227", "228", "229", "230", "231", "232", "233",
          "234",
          "235", "236", "237", "238", 160.3, "241", "242", 159.4, "245", "246", "247", "248", 156.4, "251", "252",
          "253",
          "254", "255", "256", "257", "258", "259", "260", "261", "262", "263", "264", "265", "266", 151.1, "269",
          "270",
          "271", "272", "273", 148.6, "276", "277", "278", "279", "280", "281", "282", 144.9, "285", "286", "287",
          "288",
          "289", "290", "291", "292", "293", "294", 140.8, "297", "298", "299", "300", "301", "302", "303",
          "Taizhou University", "304", 138, "307", "308", "309", 136.4, "312", "313", "314", 135.1, 135, "319", "320",
          134.4, "323", "324", "325", "326", "327", 131.7, "333", 131.1, "Wuyi University", "339", "340", "341", 128.5,
          128,
          "346", 127.2, "349", 126.5, "352", "353", "354", "355", 124.8, "358", "359", "360", "361", "362", "363",
          "364",
          122.9, "367", "368", "369", "370", "371", "372", 121, "375", 120.7, "378", "379", "380", "381", "382", "383",
          "384", "385", "392", 117.4, "398", 117.1, "401", "405", 115.9, "408", 115.6, "411", "412", 115, 114.8, "417",
          "418", "419", "420", "421", "422", "423", 113.3, "426", "427", 112.6, 112.4, 112, "434", "435", "436", "437",
          "438", "439", "440", 110.3, 110, 109.9, "451", "452", "453", "454", "455", 108.4, "458", "459", "460", "461",
          "462", "463", "464", 106.6, "470", "471", "472", "473", "474", "475", "476", 104.6, "479", "480", "481",
          "482",
          "483", "484", 102.8, "490", "491", "492", "493", "494", "495", "496", "497", "498", 100.3, "504", 99.5, 99.4,
          "509", "510", "511", 98.6, 98.1, "516", 97.7, "519", 97.5, "522", "523", "524", "525", 96.3, "528", 96.1,
          "531",
          "532", "533", "534", "535", 94, 93.9, "546", "547", "548", "549", "550", "551", "552", 89.9, "555", "556",
          "557",
          88.5, "560", "561", "562", "563", "564", "565", "566", "567", "568", "569", 84.5, "572", "573", "574", "575",
          "576", "577", "578", "579", "580", "581", "582", "583", "584", "585", "586", "587", "588", 60.5, "591", "592",
          "593", "594", 9, "2024-04-18T00:00:00+08:00", "logo\u002Fannual\u002Fbcur\u002F2024.png",
          "软科中国大学排名于2015年首次发布，多年来以专业、客观、透明的优势赢得了高等教育领域内外的广泛关注和认可，已经成为具有重要社会影响力和权威参考价值的中国大学排名领先品牌。软科中国大学排名以服务中国高等教育发展和进步为导向，采用数百项指标变量对中国大学进行全方位、分类别、监测式评价，向学生、家长和全社会提供及时、可靠、丰富的中国高校可比信息。",
          "学生、家长、高校管理人员、高教研究人员等", 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015,
          "logo\u002FindAnalysis\u002Fbcur.png", "中国大学排名", "国内", "大学"]

    dict_data = dict(zip(a_, b_))
    if r.status_code == 200:
        r.encoding = 'utf-8'
        content = r.text
        # print(content)
        colleges = []
        while content.find('univNameCn:"') != -1:
            acollege = []
            # 切出校徽地址
            content = content[content.find('univLogo:"') + 10:]
            collegeLogo = content[:content.find('"')]
            acollege.append(collegeLogo)
            # 切分出大学名称
            content = content[content.find('univNameCn:"') + 12:]
            collegeName = content[:content.find('"')]
            acollege.append(collegeName)
            # 切分出大学英文名称
            content = content[content.find('univNameEn:"') + 12:]
            collegeENName = content[:content.find('"')]
            acollege.append(collegeENName)
            # 切分出标签
            content = content[content.find('univTags:[') + 10:]
            collegeTag1 = content[:content.find(',')]
            if collegeTag1 == ']':
                acollege.append(None)
            elif collegeTag1[-1] == ']':
                acollege.append(dict_data[collegeTag1[0]])
            else:
                content = content[content.find(',') + 1:]
                collegeTag2 = content[:content.find(',')]
                if collegeTag2[-1] == ']':
                    acollege.append(dict_data[collegeTag1] + '/' + dict_data[collegeTag2[0]])
                else:
                    content = content[content.find(',') + 1:]
                    collegeTag3 = content[:content.find(']')]
                    acollege.append(
                        dict_data[collegeTag1] + '/' + dict_data[collegeTag2] + '/' + dict_data[collegeTag3])
            # 切分出类型
            content = content[content.find('univCategory:') + 13:]
            collegeCategory = content[:content.find(',')]
            acollege.append(dict_data[collegeCategory])
            # 切分出省份
            content = content[content.find('province:') + 9:]
            province = content[:content.find(',')]
            acollege.append(dict_data[province])
            # 切分出总分
            content = content[content.find('score:') + 6:]
            score = content[:content.find(',')]
            if score.isalpha():  # isalpha判断是否字母
                if type(dict_data[score]) == float or type(dict_data[score]) == int:
                    acollege.append(float(dict_data[score]))
                else:
                    acollege.append(float(dict_data[score].strip('"')))
            elif '_' in score or '$' in score:
                if type(dict_data[score]) == float or type(dict_data[score]) == int:
                    acollege.append(float(dict_data[score]))
                else:
                    acollege.append(float(dict_data[score].strip('"')))
            else:
                acollege.append(float(score))
            # 切分出排名
            content = content[content.find('ranking:') + 8:]
            ranking = content[:content.find(',')]
            acollege.append(int(dict_data[ranking]))
            # 切分出办学层次
            content = content[content.find('indData:{"536":') + 15:]
            level = content[:content.find(',')]
            if len(level) == 2:
                acollege.append(float(dict_data[level]))
            elif level == 'a':
                acollege.append(None)
            else:
                acollege.append(float(level.strip('"')))
            # 将每个大学的信息数据加入到colleges列表中
            colleges.append(acollege)

        data = []

        for college in colleges:
            dict_ = {}
            dict_['rank'] = college[-2]
            dict_['cn_name'] = college[1]
            dict_['en_name'] = college[2]
            dict_['tags'] = college[3]
            dict_['province'] = college[-4]
            dict_['type'] = college[-5]
            dict_['score'] = college[-3]
            logo_str = college[0]
            dict_['logo_url'] = logo_str[logo_str.find('u002F') + 5:]
            dict_['level'] = college[-1]
            data.append(dict_)
        try:
            crawl_college_logo()
            bulk_insert_colleges(data)
            return JsonResponse({'code':200,'msg': 'success', 'data': None})
        except Exception as e:
            return JsonResponse({'msg': 'An error occurred: {}'.format(e)})
