let YuluConsumerApplication = Java.use("app.yulu.bike.YuluConsumerApplication");
YuluConsumerApplication["getOmniLockKey"].implementation = function () {
    console.log('getOmniLockKey is called');
    let ret = this.getOmniLockKey();
    console.log('getOmniLockKey ret value is ' + ret);
    return ret;
};