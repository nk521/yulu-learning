var DeviceInfo = Java.use("app.yulu.bike.lease.models.DeviceInfo");
DeviceInfo["getEncryptedData"].implementation = function () {
    console.log('getEncryptedData is called');
    var ret = this.getEncryptedData();
    console.log('getEncryptedData ret value is ' + ret);
    return ret;
};