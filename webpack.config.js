const path = require('path');

module.exports = {
    mode: 'production', // Set the mode to production for optimized builds
    entry: './static/js/scripts.js', // Corrected entry point
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'static/js') // Output directory to match your structure
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
