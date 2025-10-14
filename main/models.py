# DB 구성하는 곳
from main import db


#####################################################################################

# primary_key = 해당 컬럼을 기본키로 설정
#               보통 id 컬럼에 많이 사용함
#               중복, NULL 불가

# unique = 해당 컬럼 값이 테이블 안에서 유일해야함
#          이메일, 주민등록번호 같은 데이터에 주로 사용

# nullable = NULL 값을 허용할지 정할수 있음
#            False로 설정시 값이 들어가야함
#            비울수 없는 컬럼에서 사용해야함

# autoincrement = 정수형 컬럼에서 주로 사용, 새 레코드가 들어올 때마다 값이 자동으로 증가함
#                 주로 id컬럼에서 사용함

# ondelete='CASCADE' = 글 작성자가 탈퇴시 작성했던 글 삭제
#                      그냥 두면 오류가 발생할수 있기 때문에 삭제

#####################################################################################


# 유저모델 생성
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # db에 생성된 순서로 부여되는 id
    userid = db.Column(db.String(50), unique=True, nullable=False)  # user 가 회원 생성시 작성하는 로그인을 위한 id / 필수입력
    password = db.Column(db.String(200), nullable=False)  # 비밀번호  / 필수입력
    username = db.Column(db.String(50), nullable=False)  # 닉네임 / 필수입력
    email = db.Column(db.String(100), unique=True, nullable=False)  # 이메일 / 필수입력
    phone = db.Column(db.String(20), unique=True, nullable=False)  # 전화번호 / 필수입력
    address = db.Column(db.String(200), nullable=False)  # 주소 / 필수입력
    admin = db.Column(db.Boolean, nullable=False, default=False)  # 어드민 여부 / 필수 입력
    image = db.Column(db.String(200), nullable=True, default='user_img/default.jpg')


# 판매모델 생성
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # db에 생성된 순서로 부여되는 id
    title = db.Column(db.String(200), nullable=False)  # 제목 / 필수입력
    content = db.Column(db.Text(), nullable=False)  # 글 내용 / 필수입력
    create_date = db.Column(db.DateTime, nullable=False)  # 작성일, 시각 / 자동생성
    modify_date = db.Column(db.DateTime, nullable=True)  # 글 수정시 수정시각 알려줌
    price = db.Column(db.Integer, nullable=False)  # 가격 / 필수입력
    discount = db.Column(db.Integer, nullable=True)  # 할인율저장 / 필수아님
    tags = db.Column(db.String(50), nullable=False, default='')

    # 작성자를 참조
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)  # 사용자 삭제시 작성글 삭제
    user = db.relationship('User', backref=db.backref('Product_set'))  # Product 에서 user(작성자)를 참조

    # 이미지 여러장을 올리기 위해서 생성한 db 참조
    images = db.relationship('ProductImage', backref='product', cascade="all, delete-orphan")


class ProductImage(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id', ondelete='CASCADE'), nullable=False)
    img_path = db.Column(db.String(200), nullable=True,
                         default='product_img/상품기본.gif')  # 이미지 삽입시 사진이 아니라 이미지 저장 경로 추적 / 필수입력 아님


# 댓글모델 생성
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # db에 생성된 순서로 부여되는 id
    content = db.Column(db.Text(), nullable=False)  # 코멘트 내용 / 필수입력
    create_date = db.Column(db.DateTime, nullable=False)  # 작성시각 / 자동생성
    modify_date = db.Column(db.DateTime, nullable=True)  # 수정시 수정한 시간 생성

    product_id = db.Column(db.Integer, db.ForeignKey('product.id', ondelete='CASCADE'))  # 상품 글이 삭제되면 코멘트 자동 삭제
    product = db.relationship(Product, backref=db.backref('comment_set'))  # 판매글 작석자 참조를 통해서 판매글 접근

    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'),
                        nullable=False)  # 코멘트 작성자 계정 삭제시 코멘트 자동 삭제
    user = db.relationship('User', backref=db.backref('comment_set'))  # 댓글 작성자 참조
