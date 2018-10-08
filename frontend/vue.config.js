//var webpack = require('webpack');

module.exports = {
    pages: {
        trainingMap: {
            entry: 'src/trainingmap/main.js',
            template: 'public/trainingmap.html',
            filename: 'trainingmap.html',
        }
    },
    
    css: {
        extract: false,
        sourceMap: false
    },

    baseUrl: '/static/',
    outputDir: 'static',
    assetsDir: undefined,
    productionSourceMap: undefined,
    parallel: undefined,
    
    configureWebpack: function (config) {
        // expose the init function as a global 
        config.output.library = '[name]App';
        config.output.libraryTarget = 'var';
        config.output.libraryExport = 'default';
        
        // if production, remove the cache-hint hash from file names
        // UPDATE: I was wondering why this was nuts by default,
        // answer is iOS sucks and will never, ever replace cached JS!
        // no, clearly we should ignore the HTTP spec for caching and
        // remove manual refreshing because load time is the most important 
        // metric ever. good job lads.

        //if (process.env.NODE_ENV === 'production') {
        //    config.output.filename = 'js/[name].js';
        //    config.output.chunkFilename = 'js/[name].js';
        //}

    },
    chainWebpack: function (config) {
        // remove hashes from the end of compiled image names
        config.module.rule('images').use('url-loader').options({
            limit: 8,
            name: 'img/[name].[ext]'
        });
        config.module.rule('svg').use('file-loader').options({
            name: 'img/[name].[ext]'
        });
    
        if (process.env.NODE_ENV != 'production') {
            // in dev mode, copy over the fake index.html page
            config.plugin('copy').tap(function (args) {
                args[0][0].ignore = [];
                return args;
            });
        }
        
    },

};
