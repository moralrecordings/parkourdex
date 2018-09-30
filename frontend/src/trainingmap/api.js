var fetchWrap = function (path, base_url, success, failure) {
    fetch(`${base_url}${path}`, {
        credentials: 'include',   
    }).then(function (response) {
        if (!response.ok) {
            throw new Error(`Remote response was a ${response.status}`);
        }
        var contentType = response.headers.get("Content-Type");
        if (!(contentType && contentType.includes("application/json"))) {
            throw new TypeError('Remote response did not have the content type application/json');
        }
        response.json().then(success);
    }).catch(function (error) {
        failure(error);
    });
};

var fetchFeatureCategories = function (base_url, success, failure) {
    var formatter = function (raw_data) {
        success(raw_data);
    };
    fetchWrap('/api/v1/feature_categories.json', base_url, formatter, failure);
};

export {
    fetchFeatureCategories
}
