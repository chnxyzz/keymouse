import pywinio
import time
import atexit

# KeyBoard Commands
# Command port
KBC_KEY_CMD = 0x64
# Data port
KBC_KEY_DATA = 0x60

g_winio = None

def get_winio():
    global g_winio

    if g_winio is None:
            g_winio = pywinio.WinIO()
            def __clear_winio():
                    global g_winio
                    g_winio = None
            atexit.register(__clear_winio)

    return g_winio

def wait_for_buffer_empty():
    '''
    Wait keyboard buffer empty
    '''

    winio = get_winio()

    dwRegVal = 0x02
    while (dwRegVal & 0x02):
            dwRegVal = winio.get_port_byte(KBC_KEY_CMD)

def key_down(scancode):
    winio = get_winio()

    wait_for_buffer_empty();
    winio.set_port_byte(KBC_KEY_CMD, 0xd2);
    wait_for_buffer_empty();
    winio.set_port_byte(KBC_KEY_DATA, scancode)

def SPkey_down(scancode):
    winio = get_winio()

    wait_for_buffer_empty();
    winio.set_port_byte(KBC_KEY_CMD, 0xd2);
    wait_for_buffer_empty();
    winio.set_port_byte(KBC_KEY_DATA, 0xe0)
    wait_for_buffer_empty();
    winio.set_port_byte(KBC_KEY_CMD, 0xd2);
    wait_for_buffer_empty();
    winio.set_port_byte(KBC_KEY_DATA, scancode)

def key_up(scancode):
    winio = get_winio()

    wait_for_buffer_empty();
    winio.set_port_byte( KBC_KEY_CMD, 0xd2);
    wait_for_buffer_empty();
    winio.set_port_byte( KBC_KEY_DATA, scancode | 0x80);

def SPkey_up(scancode):
    winio = get_winio()

    wait_for_buffer_empty();
    winio.set_port_byte(KBC_KEY_CMD, 0xd2);
    wait_for_buffer_empty();
    winio.set_port_byte(KBC_KEY_DATA, 0xe0)
    wait_for_buffer_empty();
    winio.set_port_byte(KBC_KEY_CMD, 0xd2);
    wait_for_buffer_empty();
    winio.set_port_byte(KBC_KEY_DATA, scancode | 0x80)

def mouse_down():
    winio = get_winio()

    wait_for_buffer_empty();
    winio.set_port_byte(KBC_KEY_CMD, 0xd3);
    wait_for_buffer_empty();
    winio.set_port_dword(KBC_KEY_DATA, 0x09)

def mouse_up():
    winio = get_winio()

    wait_for_buffer_empty();
    winio.set_port_byte(KBC_KEY_CMD, 0xd3);
    wait_for_buffer_empty();
    winio.set_port_dword(KBC_KEY_DATA, 0x08)

def key_press(scancode, press_time = 0.05):
    key_down( scancode )
    time.sleep( press_time )
    key_up( scancode )
    time.sleep(press_time)

def SPkey_press(scancode, press_time = 0.05):
    SPkey_down( scancode )
    time.sleep( press_time )
    SPkey_up( scancode )
    time.sleep(press_time)

def mouse_clicked(clicked_time = 0.05):
    mouse_down()
    time.sleep( clicked_time )
    mouse_up()
    time.sleep( clicked_time )
