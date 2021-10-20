
def test_id():
    id_database = ["001", "002", "007", "009", "117", "229"]
    print(id_database.index("001"))
    return id_database


def test_temp_pulse():
    # verify the body temp and pulse in the range or not
    body_temp = 98
    pulse = 120
    assert type(body_temp) == int
    assert body_temp > 88
    assert pulse > 111
    print("High Temperature and Pulse Alert ....")


def mask_status(var):
    assert type(var) == int
    return var

def test_mask():
    assert mask_status(0) == False
    assert mask_status(1) == True

