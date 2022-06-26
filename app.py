# import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from baseCore.base import Session
from baseCore.baseModels import (ExecOne, ExecutorService, Filter, User,
                  UserFeedback, UserOrder, UserVerificationSession)
from models import Feed, PostedUser, PostOrder, SendOrder, CreatedUser
from random import randint


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


# Отправка фильтров
@app.get('/api/filters')
def getfilters():
    return [i for i in Session.query(Filter)]


# Отзывы
# Прием отзыва
@app.post('/api/feeds')
def postfeeds(feedObject: Feed):
    if feedObject.serviceid in set(i.serviceid
                                   for i in Session.query(UserOrder).filter_by(
                                       userid=feedObject.userid)):
        Session.add(
            UserFeedback(mark=feedObject.mark,
                         feed=feedObject.feed,
                         userid=feedObject.userid,
                         serviceid=feedObject.serviceid))
        Session.commit()
        return "OK"
    return "Вы должны посетить это место, прежде чем писать отзыв"


# Отправка отзывов
@app.get('/api/feeds')
def getfeeds(serviceid: int):
    return [
        Feed(name=Session.query(User).get(i.userid).name,
             id=i.id,
             mark=i.mark,
             feed=i.feed)
        for i in Session.query(UserFeedback).filter_by(serviceid=serviceid)
    ]


# Сервисы
# Отправка карточек сервисов
@app.get('/api/services')
def getservices():
    return [i for i in Session.query(ExecutorService)]


# Отправка услуг сервисов
@app.get('/api/execs')
def getexecs(parrentserviceid: int):
    return [
        i for i in Session.query(ExecOne).filter_by(
            parrentserviceid=parrentserviceid)
    ]


# Заказы
# Отправка заказов
@app.get('/api/orders')
def getorders(userid: int):
    return [
        SendOrder(id=i.id,
                  ename=Session.query(ExecOne).get(i.uslugaid).name,
                  sname=Session.query(ExecutorService).get(i.serviceid).name,
                  price=Session.query(ExecOne).get(i.uslugaid).price,
                  serviceid=i.serviceid,
                  accepted=i.accepted,
                  isCompleted=i.isCompleted)
        for i in Session.query(UserOrder).filter_by(userid=userid)
    ]


# Прием зказавов
@app.post('/api/orders')
def postorder(order: PostOrder):
    if Session.query(ExecOne).get(order.uslugaid).status == True:
        Session.add(
            UserOrder(userid=order.userid,
                      uslugaid=order.uslugaid,
                      runtime=order.runtime,
                      serviceid=Session.query(ExecOne).get(
                          order.uslugaid).parrentserviceid))
        Session.commit()
        return "OK"
    return "No such service"


# Пользователь
# Получение пользователя
@app.get('/api/user')
def getuser(userid: int):
    return Session.query(User).filter_by(id=userid)[0]


# Регистрация пользователя
@app.post('/api/user')
def postuser(verObject: CreatedUser):
    code = randint(100000, 987654)
    Session.add(
        UserVerificationSession(phone=verObject.phone,
                                code=code))
    Session.commit()
    print(code)
    return "OK"


@app.post('/api/verification')
def postverification(verObject: CreatedUser):
    userSession = Session.query(UserVerificationSession).filter_by(
        phone=verObject.phone)[0]
    if verObject.code == userSession.code:
        Session.delete(userSession)
        Session.add(User(phone=verObject.phone))
        Session.commit()
        return Session.query(User).filter_by(phone=verObject.phone)[0]
    return "error"


# if __name__ == '__main__':
#     uvicorn.run('app:app', host='0.0.0.0', port=80, reload=True)
