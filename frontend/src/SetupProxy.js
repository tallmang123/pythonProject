const createProxyMiddleware = require('http-proxy-middleware');

//location.href 사용하는 경우 package.json에 설정한 프록시가 정상적으로 동작하지 않는 경우가 있어 수동으로 해당 url에 대한 프록시 처리 진행
module.exports = function(app) {
  app.use(
    '/googleLogin',
    createProxyMiddleware({
      target: 'http://localhost:5000',
      changeOrigin: true,
    })
  );
};