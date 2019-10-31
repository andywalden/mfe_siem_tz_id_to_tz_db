
def nitro_tz(tz_id):
    """Maps McAfee SIEM/Nitro ESM internal timezone IDs to 
        the tz database at: http://web.cs.ucla.edu/~eggert/tz/tz-link.htm
    
        Args:
            tz_id (str/int): McAfee ESM internal timezone ID
            
        Returns:
            timezone name (str)
    
    """
    return tz_map[tz_id]

    tz_map = {1: 'Pacific/Pago_Pago',
                2: 'Pacific/Honolulu',
                3: 'America/Anchorage'     
                4: 'America/Los_Angeles'  
                5: 'America/Phoenix'      
                6: 'America/Chihuahua'    
                7: 'America/Denver''     
                8: 'America/Guatemala'    
                9: 'America/Chicago'    
                10: 'America/Mexico_City' 
                11: 'America/Regina'     
                12: 'America/Bogota'     
                13: 'America/New_York'    
                14: 'America/Indiana/Indianapolis' 
                15: 'America/Halifax'     
                16: 'America/Caracas'     
                17: 'America/Santiago'    
                18: 'America/St_Johns'     
                19: 'America/Sao_Paulo' 
                20: 'America/Buenos_Aires'     
                21: 'America/Godthab'     
                22: 'Atlantic/South_Georgia' 
                23: 'Atlantic/Azores'     
                24: 'Atlantic/Cape_Verde'     
                25: 'Africa/Casablanca'     
                26: 'Etc/UTC' 
                27: 'Europe/Amsterdam' 
                28: 'Europe/Belgrade' 
                29: 'Europe/Brussels' 
                30: 'Europe/Warsaw' 
                31: 'Africa/Tripoli' 
                32: 'Europe/Athens' 
                33: 'Europe/Bucharest'     
                34: 'Africa/Cairo'     
                35: 'Africa/Maputo' 
                36: 'Europe/Helsinki' 
                37: 'Asia/Jerusalem'     
                38: 'Asia/Baghdad'     
                39: 'Asia/Riyadh',
                40: 'Europe/Moscow'     
                41: 'Africa/Nairobi'     
                42: 'Asia/Tehran'     
                43: 'Asia/Dubai',
                44: 'Asia/Baku',
                45: 'Asia/Kabul'     
                46: 'Asia/Yekaterinburg'     
                47: 'Asia/Karachi',
                48: 'Asia/Kolkata',
                49: 'Asia/Kathmandu' 
                50: 'Asia/Almaty'     
                51: 'Asia/Dhaka' 
                52: 'Asia/Colombo' 
                53: 'Asia/Rangoon'     
                54: 'Asia/Bangkok'     
                55: 'Asia/Krasnoyarsk'     
                56: 'Asia/Shanghai' 
                57: 'Asia/Irkutsk'     
                58: 'Asia/Singapore' 
                59: 'Australia/Perth'     
                60: 'Asia/Taipei'     
                61: 'Asia/Tokyo' 
                62: 'Asia/Seoul'     
                63: 'Asia/Yakutsk'     
                64: 'Australia/Adelaide'     
                65: 'Australia/Darwin'     
                66: 'Australia/Brisbane'     
                67: 'Australia/Sydney',
                68: 'Pacific/Guam' 
                69: 'Australia/Hobart'     
                70: 'Asia/Vladivostok'     
                71: 'Asia/Magadan'     
                72: 'Pacific/Auckland'     
                73: 'Pacific/Fiji' 
                74: 'Pacific/Tongatapu' 
                75: 'Asia/Tbilisi'     
                76: 'Europe/Dublin',
                77: 'Europe/Istanbul'}


