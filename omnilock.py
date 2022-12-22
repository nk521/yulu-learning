from dataclasses import dataclass
import random


class CrcUtil:
    @dataclass
    class Byte:
        MIN_VALUE = -128
        MAX_VALUE = 127
        SIZE = 8

    lut1 = [0, -63, -127, 64, 1, -64, Byte.MIN_VALUE, 65, 1, -64, Byte.MIN_VALUE, 65, 0, -63, -127, 64, 1, -64, Byte.MIN_VALUE, 65, 0, -63, -127, 64, 0, -63, -127, 64, 1, -64, Byte.MIN_VALUE, 65, 1, -64, Byte.MIN_VALUE, 65, 0, -63, -127, 64, 0, -63, -127, 64, 1, -64, Byte.MIN_VALUE, 65, 0, -63, -127, 64, 1, -64, Byte.MIN_VALUE, 65, 1, -64, Byte.MIN_VALUE, 65, 0, -63, -127, 64, 1, -64, Byte.MIN_VALUE, 65, 0, -63, -127, 64, 0, -63, -127, 64, 1, -64, Byte.MIN_VALUE, 65, 0, -63, -127, 64, 1, -64, Byte.MIN_VALUE, 65, 1, -64, Byte.MIN_VALUE, 65, 0, -63, -127, 64, 0, -63, -127, 64, 1, -64, Byte.MIN_VALUE, 65, 1, -64, Byte.MIN_VALUE, 65, 0, -63, -127, 64, 1, -64, Byte.MIN_VALUE, 65, 0, -63, -127, 64, 0, -63, -127, 64, 1, -64, Byte.MIN_VALUE, 65, 1, -64, Byte.MIN_VALUE, 65, 0, -63, -127, 64, 0, -63, -127, 64, 1, -64, Byte.MIN_VALUE, 65, 0, -63, -127, 64, 1, -64, Byte.MIN_VALUE, 65, 1, -64, Byte.MIN_VALUE, 65, 0, -63, -127, 64, 0, -63, -127, 64, 1, -64, Byte.MIN_VALUE, 65, 1, -64, Byte.MIN_VALUE, 65, 0, -63, -127, 64, 1, -64, Byte.MIN_VALUE, 65, 0, -63, -127, 64, 0, -63, -127, 64, 1, -64, Byte.MIN_VALUE, 65, 0, -63, -127, 64, 1, -64, Byte.MIN_VALUE, 65, 1, -64, Byte.MIN_VALUE, 65, 0, -63, -127, 64, 1, -64, Byte.MIN_VALUE, 65, 0, -63, -127, 64, 0, -63, -127, 64, 1, -64, Byte.MIN_VALUE, 65, 1, -64, Byte.MIN_VALUE, 65, 0, -63, -127, 64, 0, -63, -127, 64, 1, -64, Byte.MIN_VALUE, 65, 0, -63, -127, 64, 1, -64, Byte.MIN_VALUE, 65, 1, -64, Byte.MIN_VALUE, 65, 0, -63, -127, 64]
    lut2 = [0, -64, -63, 1, -61, 3, 2, -62, -58, 6, 7, -57, 5, -59, -60, 4, -52, 12, 13, -51, 15, -49, -50, 14, 10, -54, -53, 11, -55, 9, 8, -56, -40, 24, 25, -2, 27, -37, -38, 26, 30, -34, -33, 31, -35, 29, 28, -36, 20, -44, -43, 21, -41, 23, 22, -42, -46, 18, 19, -45, 17, -47, -48, 16, -16, 48, 49, -15, 51, -13, -14, 50, 54, -10, -9, 55, -11, 53, 52, -12, 60, -4, -3, 61, -1, 63, 62, -2, -6, 58, 59, -5, 57, -7, -8, 56, 40, -24, -23, 41, -21, 43, 42, -22, -18, 46, 47, -17, 45, -19, -20, 44, -28, 36, 37, -27, 39, -25, -26, 38, 34, -30, -29, 35, -31, 33, 32, -32, -96, 96, 97, -95, 99, -93, -94, 98, 102, -90, -89, 103, -91, 101, 100, -92, 108, -84, -83, 109, -81, 111, 110, -82, -86, 106, 107, -85, 105, -87, -88, 104, 120, -72, -71, 121, -69, 123, 122, -70, -66, 126, Byte.MAX_VALUE, -65, 125, -67, -68, 124, -76, 116, 117, -75, 119, -73, -74, 118, 114, -78, -77, 115, -79, 113, 112, -80, 80, -112, -111, 81, -109, 83, 82, -110, -106, 86, 87, -105, 85, -107, -108, 84, -100, 92, 93, -99, 95, -97, -98, 94, 90, -102, -101, 91, -103, 89, 88, -104, -120, 72, 73, -119, 75, -117, -118, 74, 78, -114, -113, 79, -115, 77, 76, -116, 68, -124, -123, 69, -121, 71, 70, -122, -126, 66, 67, -125, 65, -127, Byte.MIN_VALUE, 64]

    def somecrc(self, data: bytearray):
        """
        int length = data.length;
        int i = 0;
        int i2 = 255;
        int i3 = 255;
        while (i < length) {
            int i4 = (i3 ^ data[0 + i]) & 255;
            int i5 = i2 ^ f6820a[i4];
            int i6 = f6821b[i4];
            i++;
            i3 = i5 == 1 ? 1 : 0;
            i2 = i6;
        }
        return ((i2 & 255) << 8) | (i3 & 255 & 65535);
        """

        length = len(data)
        i, i2, i3 = 0, 255, 255
        while i < length:
            i4 = (i3 ^ data[i]) & 255
            i5 = i2 ^ self.lut1[i4]
            i6 = self.lut2[i4]
            i += 1
            i3 = 1 if i5 == 1 else 0
            i2 = i6

        return ((i2 & 255) << 8) | (i3 & 255 & 65535)


class CommandUtil:

    @staticmethod
    def process_command(command: bytearray):
        bArr = bytearray(len(command))
        bArr[0] = command[0]
        bArr[1] = command[1] + 50

        for i in range(2, len(command)):
            bArr[i] = command[i] ^ command[1]

        return bArr

    @staticmethod
    def some(ori: bytearray):
        """
        byte[] bArr = new byte[ori.length + 2];
        int m12574b = CRCUtil.m12574b(ori);
        for (int i = 0; i < ori.length; i++) {
            bArr[i] = ori[i];
        }
        bArr[ori.length] = (byte) ((m12574b >> 8) & 255);
        bArr[ori.length + 1] = (byte) (m12574b & 255);
        return bArr;
        """

        bArr = bytearray(len(ori) + 2)
        crc = CrcUtil().somecrc(ori)
        for i in range(0, len(ori)):
            bArr[i] = ori[i]

        bArr[len(ori)] = ((crc >> 8) & 255)
        bArr[len(ori) + 1] = (crc & 255)
        return bArr


def get_omni_lock_status_key() -> bytearray:
    """
    let YuluConsumerApplication = Java.use("app.yulu.bike.YuluConsumerApplication");
    YuluConsumerApplication["getOmniLockKey"].implementation = function () {
        console.log('getOmniLockKey is called');
        let ret = this.getOmniLockKey();
        console.log('getOmniLockKey ret value is ' + ret);
        return ret;
    };
    """
    ...


def send_ble_characteristics() -> None:
    some_var = 0
    a: bytearray = CommandUtil.some(CommandUtil.process_command(bytearray([-2, random.randint(0, 255-1) & 255, some_var, get_omni_lock_status_key(), 0])))
    # write this characteristic to ...
    print(a)
