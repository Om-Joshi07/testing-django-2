

import requests as r

def soil_data_fetch(latitude, longitude):
    try:
        R = r.get(f"https://soil.narc.gov.np/soil/api/?lat={latitude}&lon={longitude}").json()

        if not R or 'coord' not in R:
            print("Soil data not available.")
            return "❌ The soil information is not available."

        
        response = (
            f"🧾 Soil Report for {R['palika']}, {R['district']} District, {R['province']} Province\n\n"

            "📍 Location Details:\n"
            f"  Latitude  : {R['coord']['lat']}\n"
            f"  Longitude : {R['coord']['lon']}\n"
            f"  Elevation : {R['coord']['elevation']} m\n\n"

            "🌱 Soil Composition:\n"
            f"  pH                 : {R['ph']}\n"
            f"  Organic Matter     : {R['organic_matter']}\n"
            f"  Total Nitrogen     : {R['total_nitrogen']}\n"
            f"  Potassium (K)      : {R['potassium']}\n"
            f"  Phosphorus (P₂O₅)  : {R['p2o5']}\n"
            f"  Boron              : {R['boron'][0:4] +' mg/kg'}\n"
            f"  Zinc               : {R['zinc'][0:4] +' mg/kg'}\n"


            "🧱 Soil Texture:\n"
            f"  Sand  : {R['sand']}\n"
            f"  Clay  : {R['clay']}\n"
            f"  Silt  : {R['slit']}\n\n"

            "🪨 Parent Material:\n"
            f"  {R['parentsoil']}\n"
        )

        return response

    except Exception as e:
        return f"❌ Failed to fetch soil report: {e}"

