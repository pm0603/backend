from urllib.parse import urlencode, quote_plus, unquote
from urllib.request import urlopen, Request

import xmltodict
from rest_framework.response import Response
from rest_framework.views import APIView

from config.settings import config
from .models import ContentList

decode_key = unquote(config['API']['API_key'])
global_url = 'http://www.culture.go.kr/openapi/rest/publicperformancedisplays/'


def xml_parser_db_save(request):
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()
    data = xmltodict.parse(response_body)

    item_path = data['response']['msgBody']['perforList']

    for index, item in enumerate(item_path):
        item_path_index = item_path[index]
        seq = item_path_index['seq']
        title = item_path_index['title']
        place = item_path_index['place']
        startDate = item_path_index['startDate']
        endDate = item_path_index['endDate']
        realmName = item_path_index['realmName']
        area = item_path_index['area']
        thumbnail = item_path_index['thumbnail']
        gpsX = item_path_index['gpsX']
        gpsY = item_path_index['gpsY']

        ContentList.objects.get_or_create(
            seq=seq,
            title=title,
            place=place,
            startDate=startDate,
            endDate=endDate,
            realmName=realmName,
            area=area,
            thumbnail=thumbnail,
            gpsX=gpsX,
            gpsY=gpsY,
        )
    return data


class Area(APIView):
    def get(self, request):
        keyword = request.GET.get('keyword')
        rows = request.GET.get('rows')
        url = global_url + 'area'
        queryParams = '?' + urlencode({quote_plus('ServiceKey'): decode_key,
                                       quote_plus('sido'): keyword,
                                       quote_plus('gugun'): '',
                                       quote_plus('rows'): rows})
        """
        sido = 지역 (서울, 대구, 등..)
        gugun = 구/군 (Null)으로 하면 결과가 더 잘나옴.
        """
        request = Request(url + queryParams)
        data = xml_parser_db_save(request)
        return Response(data)


class Genre(APIView):
    def get(self, request):
        keyword = request.GET.get('keyword')
        Code = request.GET.get('code')
        rows = request.GET.get('rows')
        url = global_url + 'realm'
        queryParams = '?' + urlencode({quote_plus('ServiceKey'): decode_key,
                                       quote_plus('realmCode'): Code,
                                       quote_plus('keyword'): keyword,
                                       quote_plus('rows'): rows})
        """
        A = 연극
        B = 음악 국악 콘서트
        C = 무용
        D = 미술
        """
        request = Request(url + queryParams)
        data = xml_parser_db_save(request)
        return Response(data)


class Period(APIView):
    def get(self, request):
        start = request.GET.get('start')
        end = request.GET.get('end')
        rows = request.GET.get('rows')
        url = global_url + 'period'
        queryParams = '?' + urlencode({quote_plus('ServiceKey'): decode_key,
                                       quote_plus('from'): start,
                                       quote_plus('to'): end,
                                       quote_plus('rows'): rows})
        """
        sido = 지역 (서울, 대구, 등..)
        gugun = 구/군 (Null)으로 하면 결과가 더 잘나옴.
        """
        request = Request(url + queryParams)
        data = xml_parser_db_save(request)
        return Response(data)


class Detail(APIView):
    def get(self, request):
        seq = request.GET.get('seq')
        url = global_url + 'd/'
        queryParams = '?' + urlencode({quote_plus('ServiceKey'): decode_key,
                                       quote_plus('seq'): seq})
        """
        sido = 지역 (서울, 대구, 등..)
        gugun = 구/군 (Null)으로 하면 결과가 더 잘나옴.
        """
        request = Request(url + queryParams)
        request.get_method = lambda: 'GET'
        response_body = urlopen(request).read()
        data = xmltodict.parse(response_body)

        item_path = data['response']['msgBody']['perforInfo']

        seq = item_path['seq']
        title = item_path['title']
        startDate = item_path['startDate']
        endDate = item_path['endDate']
        place = item_path['place']
        realmName = item_path['realmName']
        area = item_path['area']
        price = item_path['price']
        content = item_path['contents1']
        ticket_url = item_path['url']
        phone = item_path['phone']
        thumbnail = item_path['imgUrl']
        gpsX = item_path['gpsX']
        gpsY = item_path['gpsY']
        placeUrl = item_path['placeUrl']
        placeAddr = item_path['placeAddr']
        placeSeq = item_path['placeSeq']

        ContentList.objects.filter(seq=seq).update(
            seq=seq,
            title=title,
            place=place,
            startDate=startDate,
            ticket_url=ticket_url,
            phone=phone,
            price=price,
            endDate=endDate,
            realmName=realmName,
            area=area,
            thumbnail=thumbnail,
            gpsX=gpsX,
            gpsY=gpsY,
            content=content,
            placeUrl=placeUrl,
            placeAddr=placeAddr,
            placeSeq=placeSeq,
        )
        return Response(data)
