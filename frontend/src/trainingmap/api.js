import L from 'leaflet';

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

export {
    fetchFeatureCategories,
    fetchLocations,
}
