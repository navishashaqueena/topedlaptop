import scrapy
import json


class LaptopgameSpider(scrapy.Spider):
    name = 'laptopGame'
    allowed_domains = ['www.tokopedia.com']

    def start_requests(self):
        query = [
            {
                "operationName": "SearchProductQuery",
                "variables": {
                    "params": "page=1&ob=&identifier=komputer-laptop_pc-laptop-gaming&sc=3847&user_id=0&rows=60&start=1&source=directory&device=desktop&page=1&related=true&st=product&safe_search=false",
                    "adParams": "page=1&page=1&dep_id=3847&ob=&ep=product&item=15&src=directory&device=desktop&user_id=0&minimum_item=15&start=1&no_autofill_range=5-14"
                },
                "query": "query SearchProductQuery($params: String, $adParams: String) {\n  CategoryProducts: searchProduct(params: $params) {\n    count\n    data: products {\n      id\n      url\n      imageUrl: image_url\n      imageUrlLarge: image_url_700\n      catId: category_id\n      gaKey: ga_key\n      countReview: count_review\n      discountPercentage: discount_percentage\n      preorder: is_preorder\n      name\n      price\n      original_price\n      rating\n      wishlist\n      labels {\n        title\n        color\n        __typename\n      }\n      badges {\n        imageUrl: image_url\n        show\n        __typename\n      }\n      shop {\n        id\n        url\n        name\n        goldmerchant: is_power_badge\n        official: is_official\n        reputation\n        clover\n        location\n        __typename\n      }\n      labelGroups: label_groups {\n        position\n        title\n        type\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  displayAdsV3(displayParams: $adParams) {\n    data {\n      id\n      ad_ref_key\n      redirect\n      sticker_id\n      sticker_image\n      productWishListUrl: product_wishlist_url\n      clickTrackUrl: product_click_url\n      shop_click_url\n      product {\n        id\n        name\n        wishlist\n        image {\n          imageUrl: s_ecs\n          trackerImageUrl: s_url\n          __typename\n        }\n        url: uri\n        relative_uri\n        price: price_format\n        campaign {\n          original_price\n          discountPercentage: discount_percentage\n          __typename\n        }\n        wholeSalePrice: wholesale_price {\n          quantityMin: quantity_min_format\n          quantityMax: quantity_max_format\n          price: price_format\n          __typename\n        }\n        count_talk_format\n        countReview: count_review_format\n        category {\n          id\n          __typename\n        }\n        preorder: product_preorder\n        product_wholesale\n        free_return\n        isNewProduct: product_new_label\n        cashback: product_cashback_rate\n        rating: product_rating\n        top_label\n        bottomLabel: bottom_label\n        __typename\n      }\n      shop {\n        image_product {\n          image_url\n          __typename\n        }\n        id\n        name\n        domain\n        location\n        city\n        tagline\n        goldmerchant: gold_shop\n        gold_shop_badge\n        official: shop_is_official\n        lucky_shop\n        uri\n        owner_id\n        is_owner\n        badges {\n          title\n          image_url\n          show\n          __typename\n        }\n        __typename\n      }\n      applinks\n      __typename\n    }\n    template {\n      isAd: is_ad\n      __typename\n    }\n    __typename\n  }\n}\n"
            }
        ]

        yield scrapy.Request(
            url='https://gql.tokopedia.com/graphql/SearchProductQuery',
            method='POST',
            headers={
                "authority": "gql.tokopedia.com",
                "accept": "*/*",
                "accept-language": "id,en-US;q=0.9,en;q=0.8",
                "content-type": "application/json",
                "iris_session_id": "d3d3LnRva29wZWRpYS5jb20=.a6d840544adaa4ae7b7dc9538a1d3de0.1650305784892",
                "origin": "https://www.tokopedia.com",
                "referer": "https://www.tokopedia.com/p/komputer-laptop/pc-laptop-gaming?page=1",
                "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"100\", \"Google Chrome\";v=\"100\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-site",
                "tkpd-userid": "0",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
                "x-device": "desktop-0.0",
                "x-source": "tokopedia-lite",
                "x-tkpd-lite-service": "zeus",
                "x-version": "0ffced9"
            },
            cookies={
                "_UUID_NONLOGIN_": "41be050a573fb6fd95dd00bcf4d589ea",
                "_UUID_NONLOGIN_.sig": "heErPjWCrJ4UFd2xmyUmHGBc0LU",
                "DID": "4e235f00104008e159a0859354ba51fae109b14e05b39c6f0a296b514785ebc67a4bbaee1a0c893da70e83d5cf309c8c",
                "DID_JS": "NGUyMzVmMDAxMDQwMDhlMTU5YTA4NTkzNTRiYTUxZmFlMTA5YjE0ZTA1YjM5YzZmMGEyOTZiNTE0Nzg1ZWJjNjdhNGJiYWVlMWEwYzg5M2RhNzBlODNkNWNmMzA5Yzhj47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=",
                "_gcl_au": "1.1.459897032.1648358453",
                "_UUID_CAS_": "5d5e12c4-c8ef-4b1a-8eac-412ae7eaca27",
                "__auc": "bc1a602d17fc9d2198a7a3ff70b",
                "_hjSessionUser_714968": "eyJpZCI6IjIzMGY1YThjLWYyZWMtNTA3Yy1iOTk0LWM1YTczZjMwMjE2NiIsImNyZWF0ZWQiOjE2NDgzNTg0NzIxOTAsImV4aXN0aW5nIjp0cnVlfQ==",
                "S_L_05737eefd8d05b3537a6d33fb6c50614": "5778fac94ebcab6f27879a450dcf86da~20220626115918",
                "_fbp": "fb.1.1648443729399.2015805666",
                "_gcl_aw": "GCL.1648464836.CjwKCAjwuYWSBhByEiwAKd_n_gxzNcky2JLC1xRt8hUzwOg1vCGt4-xymbqfbsYSji5Q7MErH3JWbBoCq0YQAvD_BwE",
                "_gcl_dc": "GCL.1648464836.CjwKCAjwuYWSBhByEiwAKd_n_gxzNcky2JLC1xRt8hUzwOg1vCGt4-xymbqfbsYSji5Q7MErH3JWbBoCq0YQAvD_BwE",
                "_gac_UA-126956641-6": "1.1648464836.CjwKCAjwuYWSBhByEiwAKd_n_gxzNcky2JLC1xRt8hUzwOg1vCGt4-xymbqfbsYSji5Q7MErH3JWbBoCq0YQAvD_BwE",
                "_gac_UA-9801603-1": "1.1648464840.CjwKCAjwuYWSBhByEiwAKd_n_gxzNcky2JLC1xRt8hUzwOg1vCGt4-xymbqfbsYSji5Q7MErH3JWbBoCq0YQAvD_BwE",
                "shipping_notif": "0",
                "_gid": "GA1.2.395062503.1650103502",
                "_CASE_": "2871371a377169616164677f71321a377169637f713f313f71697119323832212732730326203227717f71301a3771696264657f713f3c3d34716971717f713f3227716971717f7123103c716971717f71241a37716962616162636064667f71201a37716962626660636664607f7120072a2336716971613b717f71243b2071697108280f71243221363b3c2620360c3a370f716962616162636064667f0f71203621253a30360c272a23360f71690f71613b0f717f0f710c0c272a23363d323e360f71690f71043221363b3c262036200f712e7f280f71243221363b3c2620360c3a370f7169637f0f71203621253a30360c272a23360f71690f7162663e0f717f0f710c0c272a23363d323e360f71690f71043221363b3c262036200f712e0e712e",
                "hfv_banner": "true",
                "_abck": "24CFB13A125A1CF4A2E48FDD29D37742~0~YAAQrHnqZyYbnzuAAQAARdPjPQdKTHL/Suy4+zp254Gwm6+mLsmp5szj1ioLFbmz7DG6JTuJjMjWE6tfR7RPxGxrvnqBCqchRsaPwh3osOgMgY5BZEokSQOqDys472v1GiOWjRNgAEoUALwXVfzBn0mFBlpvBU2bgPvwwH9DYPkmBW1dkAfLulTbZkUMQR53JKVvbGQlU6zRRBfBiqJhvdr7bjxsjKUjz/s4cZFw0nu0tHtcnJoIp/49JWOFX7vTDLaOPrd+Y1RjCSZ+V9IiAQ1+kW9L1qktZbyXBpLhh/XH9sFvaT3w3l7NO4ptWjLY1BS7E3kDLjptBMpshadpmchXvgcc206whVZhKP08I7Xk7CbMFTzr2+ns3zKB75gTRTYKvpPzwA2ffx0+Kcw9dwd9hzcU/BN9knkt~-1~-1~-1",
                "bm_sz": "4D796DC19A1F40C094B6C3BFC8CD9E3C~YAAQrHnqZycbnzuAAQAARdPjPQ9TuGjJFw99uNjkZbfR0vItp1txPxoQBtrBmbkUlXIogGoimQrWZ5xaLzg8HXb65JI1iZvcfqQP8F2aH9smq3RDlG//j5s4jVpJsaH27wcwmMth56HEfou5JuePMPgickohdWrxVcjs8iMe4PXax0jq7qgqpujncW6c4CnL6GYzUW7YgfaRilPd6RlL13DkWTkAyHVkuZlQaFbnz0Z3aICWYipoTPJD4VCDLuum5TAKe6XlYxJiEkvcLxerwnfZJ4nrKTDwr+UbrXsm4eoPGW6U1dI=~4343095~4470341",
                "_SID_Tokopedia_": "2DUQQ3z9VfY8otBluKQNOfBS5FhLObxDgIHjdQB9sLXdnsQzzp-V7pFOSGyCI77whcp42YVFCDW99yv6UwAaqx1hz5kepprt81tj1sfJBFVVGNHGtLibVRKrUHvTy_L3",
                "AMP_TOKEN": "%24NOT_FOUND",
                "__asc": "cd68d3c61803de3ed81e93296ae",
                "bm_mi": "032A653375FBF987ABA307A5C3720BB6~6bAnn+qQZRp2Ezl8N/cAahrGHZUXTh18kNS8f5gxUAICUEkqd3BpsRC+EXG1x420BxebMtWjxTK7BOBLOyys0Xd8I4e66pR8jVkaZKChrSr+ipBw6PMZ4qJpUKto8sLJ8zSNQUC+p8XZbhYA9blRn8IkGEvNs4WL7yO8kNlmr1GUHsqpDcvboSu+kSq2AxBvigprkryHRCdJU6dNteiaKaApYU6j2KdfwQ2QaL2C7hIXriRyiDmZ36e0T4CWvXrvmQ5Jqacn+hZWLg2XnYUmNvjQY0ip3vvy0h9fq+MqVKc=",
                "ak_bmsc": "0028ED461D930521EF435E8627AA1CCF~000000000000000000000000000000~YAAQtu84FzgQdwCAAQAArGP9PQ9YqFw90g/psu+vxkcztLdk5qsLijmcD09tJeIBwlJi1MS2kz6GTX5x1kKn3pTIrvAB2O8CTuhNwao61ifEOCdxk3PHQTdJQ/ssbciepF6LjctQG4DSzkfSpXcypGVN0YMAeYbh2XMOnVXAvpNehAJAjguoTNtldGW0wsix9vQh+jMxQXjZnTk3mcC+Kc32Umv7G+fGIJAMEZBkkV3scfEJuaHSdjbRSdWpLrhpUAoLEzxLif0LieWQyNUUO2a/4p22fsx6wIIBRodgTlk+/D+UkhCGz21ROBFbddwUuHKNIEfFZOY78pEERQM8iOatS+BGNpma8qKldXv37Mrmf/YGv4KlmV61sDKJcdDow2hbBIHkZcZao8GfjxbWI93ao3WU2VqcJu98Y/cz7Bc3RjBlX+NA0ZcYqNo8z1Y=",
                "_ga": "GA1.2.133170368.1648358453",
                "_dc_gtm_UA-9801603-1": "1",
                "_gat_UA-9801603-1": "1",
                "_ga_70947XW48P": "GS1.1.1650305782.25.1.1650307766.47",
                "_dc_gtm_UA-126956641-6": "1"
            },
            body=json.dumps(query),
            callback=self.parse



        )

    def parse(self, response):
        # print(response.body)
        # with open('topedlaptop.json', 'wb') as f:
        #     f.write(response.body)
        respon = json.loads(response.body)
        semuaData = respon[0].get('data').get(
            'CategoryProducts').get('data')[:]

        for data in semuaData:
            yield {
                'Total Review': data.get('countReview'),
                'Rating': data.get('rating'),
                'Diskon Presentase': data.get('discountPercentage'),
                'Nama Produk': data.get('name'),
                'Harga Asli': data.get('original_price'),
                'Harga Diskon': data.get('price'),
                'Nama Toko': data.get('shop').get('name'),
                'Lokasi Toko': data.get('shop').get('location'),
                'URL': data.get('shop').get('url'),
            }
