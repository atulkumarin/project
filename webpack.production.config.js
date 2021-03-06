var webpack = require('webpack');
var path = require('path');
var uglifyJsPlugin = webpack.optimize.UglifyJsPlugin;
var CopyWebpackPlugin = require('copy-webpack-plugin');
var ExtractTextPlugin = require("extract-text-webpack-plugin");

module.exports = {
    devtool: 'cheap-source-map',
    entry: [
        path.resolve(__dirname, 'history/main.js'),
    ],
    output: {
        path: __dirname + '/build',
        publicPath: '/',
        filename: './bundle.js'
    },
    module: {
        loaders:[
            { test: /\.jsx?$/,
                include: path.resolve(__dirname, 'history'),
                exclude: /node_modules/,
                loader: 'babel-loader',
                query: {
                    presets: ['es2015', 'stage-0', 'react']
                }
            },
            { test: /\.css$/, include: path.resolve(__dirname, 'history'), loader: 'style-loader!css-loader' },
            { test: /\.scss$/, loader: ExtractTextPlugin.extract('style', 'css?sourceMap!sass?sourceMap')},
        ]
    },
    resolve: {
        extensions: ['', '.js', '.jsx'],
    },
    sassLoader: {
        includePaths: [ 'history/style' ]
    },
    plugins: [
        new webpack.optimize.DedupePlugin(),
        new uglifyJsPlugin({
            compress: {
                warnings: false
            }
        }),
        new webpack.DefinePlugin({
            'process.env': {
                NODE_ENV: JSON.stringify('production')
            }
        }),
        new ExtractTextPlugin('main.css'),
        new CopyWebpackPlugin([
            { from: './history/index.html', to: 'index.html' },
            { from: './history/main.scss', to: 'main.css' }
        ]),
    ]
};