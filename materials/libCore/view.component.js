{% import SPICES('angular') as NG %}

{% call NG.JSLIB(MENU.name, 'libCore', ['$rootScope', '$http']) %}

    var getMsg = function(callback) {
        $rootScope.$on("MESSAGE_ON", function(event, args) {
            type = args.type;
            value = args.value;
	    callback(event, type, value);
	});
    };
    var setMsg = function(type, value) {
        args = {"type":type, "value":value};
        $rootScope.$broadcast("MESSAGE_ON", args);
    };

    function _doHttpGet(retry_count, url_path, callback) {
        $http({method: "GET", url: url_path}).
        then(function(response) {
            callback(true, response);
        }, function(response) {
            if(retry_count < 3) {
               console.log("HTTP Get Retry count:" + retry_count);
               retry_count++;
	       _doHttpGet(retry_count, url_path, callback);
	    } else {
               doGetRetryCount = 0;
	       callback(false, response);
	    }
	});
    }

    var doHttpGet = function(url, callback) {
        _doHttpGet(0, url, callback);
    };

    return {
        getMsg: getMsg,
        setMsg: setMsg,
	doHttpGet: doHttpGet
    };

{% endcall %}
