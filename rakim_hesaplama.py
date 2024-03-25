import requests
import mgrs




def rakim_hesaplama(hedef_sag, hedef_yukari, bolge_no=None, bolge_harf=None):


    bolgevekoordinat = str(bolge_no) + bolge_harf + str(hedef_sag) + str(hedef_yukari)

    try:
        m = mgrs.MGRS()
        c = bolgevekoordinat.encode()
        d = m.toLatLon(c)
        d = str(d)
        cog_element = d.replace("(", "").replace(")", "").replace(" ", "").split(",")
        enlem = cog_element[0]
        boylam = cog_element[1]

        def get_elevation(lat, lon):
            base_url = "https://api.open-elevation.com/api/v1/lookup"
            params = {
                "locations": f"{lat},{lon}",
            }
            try:
                response = requests.get(base_url, params=params)
                data = response.json()
                elevation = data["results"][0]["elevation"]
                elevation = int(elevation)
                return elevation
            except Exception as e:
                print(f"Hata: {e}")
                return 500

        latitude = enlem
        longitude = boylam
        hedef_rakim = get_elevation(latitude, longitude)
        
        return hedef_rakim
        

    except Exception as ex:
        print(f"Hata: {ex}")
        
        return 340

    