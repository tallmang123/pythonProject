from app import app, render_template


#webpack + react-router을 사용하여 flask + react 합침
#Flask 객체를 가지고 있는 app은 결국 하나의 객체이기 때문에 함수를 직접 호출하는 방법을 모르며,
#self변수에 접근할수 없기 때문에 클래스에 종속될 수 없으며 모듈범위에 있어야 한다.
#따라서 컨트롤러단에서 Flask 단독으로 사용시 클래스로 묶지 않고 단순 함수 선언으로 사용하여야 함.
@app.route('/first')
def first():
    return render_template("index.html")
