/*webpack : 여러 자바 스크립트를 모듈화하여 하나의 스크립트로 변환한다.
react, vue 는 자바스크립트 기반으로 각각 모듈화 하여 구성되고 여러개의 뷰페이지 또한 존재하기 때문에
webpack으로 말아서 이를 하나의 파일로 통합하여 사용*/
const path = require("path")

module.exports = {
    entry: [
        "regenerator-runtime/runtime.js", // async , await 사용시 regeneratorRuntime is not defined 에러 발생하여 해당 js를 통해 사용가능하게끔 처리
        "./src/index.js" // 자바 스크립트 진입 시점 . REACT사용시 해당 파일에서 라우팅이 직접 진행될수 있어 index.js로 설정
    ],
    output : { // webpack을 통하여 통합된 파일의 경로 및 파일명 설정
        filename: "flask-react-bundle.js",
        path:path.resolve(__dirname, "../static")
    },
    module :{ //webpack은 자바스크립트만 인식학 때문에 프론트에서 사용되는 css,img 등의 파일들도 자바스크립트에서 인식할 수 있도록 변경.
        devServer: {
            proxy: {
                target: 'http://localhost:5000',
            },
        },
        rules : [
            {
                test: /\.(sa|sc|c)ss$/, // 파일 타입
                use: ['style-loader','css-loader'] // 자바스크립트에서 해당 타입의 파일을 불러올수 있는 로더 정의
            },
            {
                test: /\.m?js$/,
                exclude: "/node_modules/",
                use: [{
                    loader: "babel-loader",
                    options:{
                        presets: ["@babel/preset-env", "@babel/preset-react",{
                          'plugins': ['@babel/plugin-proposal-class-properties']}] //Support for the experimental syntax 'classProperties' isn't currently enabled 에러처리
                    }
                }]
            },
            {
                test: /\.(png|jpg|ico|svg|eot|woff|woff2|ttf)$/,
                use: ['file-loader','url-loader']
            }
        ]
    }
}