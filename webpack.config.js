const path = require('path');

module.exports = {
    mode: 'development', // Set the mode to development or production
    entry: './static/scripts.js', // Entry point
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'static') // Output directory
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
devtool: 'source-map'

};
