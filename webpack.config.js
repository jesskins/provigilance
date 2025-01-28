const path = require('path');

module.exports = {
    mode: 'production',
    entry: './static/js/scripts.js',
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'static/js')
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env']
                    }
                }
            }
        ]
    },
    resolve: {
        fallback: {
            "fs": false,
            "path": false,
            "os": false
        }
    },
    devtool: 'source-map' // Use 'source-map' for better debugging
};
