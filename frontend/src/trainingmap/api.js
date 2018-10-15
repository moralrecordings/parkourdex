import L from 'leaflet';
import Cookies from 'js-cookie';

var fetchWrap = function (path, base_url, success, failure) {
    return submitWrap(path, base_url, 'GET', undefined, success, failure);
};

var submitWrap = function (path, base_url, method, body, success, failure) {
    var csrftoken = Cookies.get('csrftoken', {
        domain: base_url.split('/')[2]   
    });

    return fetch(`${base_url}${path}`, {
        credentials: 'include',
        method: method,
        body: body,
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json'
        },
    }).then(function (response) {
        var contentType = response.headers.get('Content-Type');
        if ((contentType && contentType.includes('application/json'))) {
            if (!response.ok) {
                return response.json().then(function (error) {
                    failure(error['error']);  
                });
            }
        } else {
            if (!response.ok) {
                throw new Error(`Remote response was a ${response.status}`);
            }
            throw new TypeError('Remote response did not have the content type application/json');
        }

        return response.json().then(success);
    }).catch(function (error) {
        return failure(error);
    });
};


var fetchFeatureCategories = function (base_url, success, failure) {
    var formatter = function (raw_data) {
        var data = {
            categories: [],
            features: [],
        };
        for (var i=0; i<raw_data.length; i++) {
            var category = {
                id: raw_data[i].id,
                name: raw_data[i].name,
                enabled: true,
                features: []
            };
            for (var j=0; j<raw_data[i].features.length; j++) {
                category.features.push(data.features.length);
                data.features.push({
                    id: raw_data[i].features[j].id,
                    name: raw_data[i].features[j].name,
                    description: raw_data[i].features[j].description,
                    icon: raw_data[i].features[j].icon,
                    enabled: true
                });
            }
            data.categories.push(category);
        }
        success(data);
    };
    fetchWrap('/api/v1/feature_category.json', base_url, formatter, failure);
};

var fetchLocations = function (base_url, success, failure) {
    var formatter = function (raw_data) {
        var data = raw_data.map(function (el) {
            return {
                id: el.id,
                name: el.name,
                features: el.features,
                location: L.latLng(el.location.coordinates[1], el.location.coordinates[0]),
            };
        });
        success(data);
    };
    fetchWrap('/api/v1/location.json', base_url, formatter, failure);
};

var fetchDetail = function (base_url, id, success, failure) {
    fetchWrap(`/api/v1/location/${id}.json`, base_url, success, failure);
};

var fetchLogin = function (base_url, success, failure) {
    fetchWrap('/api/v1/login.json', base_url, success, failure);
};

var submitLogin = function (base_url, body, success, failure) {
    submitWrap('/api/v1/login.json', base_url, 'POST', body, success, failure); 
};

var submitLogout = function (base_url, success, failure) {
    submitWrap('/api/v1/logout.json', base_url, 'POST', undefined, success, failure); 
};


export {
    fetchFeatureCategories,
    fetchLocations,
    fetchDetail,
    fetchLogin,
    submitLogin,
    submitLogout,
}
