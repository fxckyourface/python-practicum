import math

G0 = 9.80665

def delta_v(m0, m1, isp=300):
    if not all(math.isfinite(v) for v in (m0, m1, isp)) or not m0 >= m1 > 0 or isp <= 0:
        raise ValueError("Требуется m0 >= m1 > 0 и isp > 0")
    return isp * G0 * math.log(m0 / m1)

def flight_time(distance_km, accel):
    if not all(math.isfinite(v) for v in (distance_km, accel)) or distance_km < 0 or accel <= 0:
        raise ValueError("Требуется distance_km >= 0 и accel > 0")
    return 2 * math.sqrt(distance_km * 1000 / 2 / accel) / 3600

def fuel_needed(m_dry, target_dv, isp=300):
    if not all(math.isfinite(v) for v in (m_dry, target_dv, isp)) or m_dry <= 0 or target_dv < 0 or isp <= 0:
        raise ValueError("Требуется m_dry > 0, target_dv >= 0 и isp > 0")
    return m_dry * math.expm1(target_dv / (isp * G0))
