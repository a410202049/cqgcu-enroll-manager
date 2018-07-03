# -*- coding:utf-8 -*-
from app.models.BaseModel import Base
from app import db
from sqlalchemy import DATETIME
from sqlalchemy import Column
from datetime import datetime

class Student(Base):
    __tablename__ = 't_student'
    id = db.Column(db.Integer, primary_key=True)
    id_card_no = db.Column(db.String(20), doc=u'身份证号', unique=True)
    exam_no = db.Column(db.String(32), doc=u'考生号')
    student_no = db.Column(db.String(24), doc=u'学号')
    name = db.Column(db.String(24), doc=u'学生姓名')
    sex = db.Column(db.SMALLINT, doc=u'性别')
    mobile = db.Column(db.String(11), doc=u'手机号')
    teacher_name = db.Column(db.String(24), doc=u'班主任姓名')
    teacher_mobile = db.Column(db.String(11), doc=u'班主任手机号码')
    bed_no = db.Column(db.String(32), doc=u'寝室号')
    cloth_id = db.Column(db.Integer,doc=u'服装ID')
    is_loan = db.Column(db.Integer, doc=u'是否有贷款 0否 1是')
    loan_amt = db.Column(db.DECIMAL(12,2), doc=u'贷款金额')
    org_no = db.Column(db.String(32), doc=u'组织id')
    height = db.Column(db.String(24), doc=u'身高')
    bust = db.Column(db.String(24), doc=u'胸围')
    waist = db.Column(db.String(24), doc=u'腰围')
    shoe_size = db.Column(db.String(24), doc=u'鞋码')
    remark = db.Column(db.String(128), doc=u'备注')
    create_time = Column("create_time", DATETIME, nullable=False, default=datetime.now, doc=u'创建时间')
    update_time = Column("update_time", DATETIME, nullable=False, default=datetime.now, onupdate=datetime.now, doc=u'更新时间')

class Organization(Base):
    __tablename__ = 't_organization'
    id = db.Column(db.Integer, primary_key=True)
    serial_no = db.Column(db.String(32), doc=u'组织结构，唯一索引', unique=True)
    grade = db.Column(db.String(20), doc=u'年级')
    academy = db.Column(db.String(64), doc=u'学生所在系部')
    major = db.Column(db.String(64), doc=u'学生所在专业')
    class_name = db.Column(db.String(64), doc=u'学生所在班级')
    remark = db.Column(db.String(128), doc=u'备注')
    create_time = Column("create_time", DATETIME, nullable=False, default=datetime.now, doc=u'创建时间')
    update_time = Column("update_time", DATETIME, nullable=False, default=datetime.now, onupdate=datetime.now,
                         doc=u'更新时间')

class BedInfo(Base):
    __tablename__ = 't_bed_info'
    id = db.Column(db.Integer, primary_key=True)
    serial_no = db.Column(db.String(32), doc=u'唯一索引', unique=True)
    build_name = db.Column(db.String(32), doc=u'楼栋名称')
    floor_no = db.Column(db.String(32), doc=u'楼层编号')
    dorm_no = db.Column(db.String(32), doc=u'寝室编号')
    bed_no = db.Column(db.String(32), doc=u'床位编号')
    remark = db.Column(db.String(128), doc=u'备注')
    create_time = Column("create_time", DATETIME, nullable=False, default=datetime.now, doc=u'创建时间')
    update_time = Column("update_time", DATETIME, nullable=False, default=datetime.now, onupdate=datetime.now, doc=u'更新时间')

class RoomRule(Base):
    __tablename__ = 't_room_rule'
    id = db.Column(db.Integer, primary_key=True)
    org_no = db.Column(db.String(32), doc=u'组织结构编号')
    sex = db.Column(db.SMALLINT, doc=u'性别')
    dorm_no = db.Column(db.String(32), doc=u'寝室编号')
    bed_no = db.Column(db.String(32), doc=u'床位编号')
    remark = db.Column(db.String(128), doc=u'备注')
    create_time = Column("create_time", DATETIME, nullable=False, default=datetime.now, doc=u'创建时间')
    update_time = Column("update_time", DATETIME, nullable=False, default=datetime.now, onupdate=datetime.now, doc=u'更新时间')


class Relative(Base):
    __tablename__ = 't_relative'
    id = db.Column(db.Integer, primary_key=True)
    student_no = db.Column(db.String(20), doc=u'学号', unique=True)
    name = db.Column(db.String(24), doc=u'监护人姓名')
    relation_ship = db.Column(db.String(24), doc=u'与学生的关系')
    mobile = db.Column(db.String(11), doc=u'手机号')
    address = db.Column(db.String(128), doc=u'住址')
    address_code = db.Column(db.String(24), doc=u'邮政编码')
    create_time = Column("create_time", DATETIME, nullable=False, default=datetime.now, doc=u'创建时间')
    update_time = Column("update_time", DATETIME, nullable=False, default=datetime.now, onupdate=datetime.now, doc=u'更新时间')
    remark = db.Column(db.String(128), doc=u'备注')

class EnrollFees(Base):
    __tablename__ = 't_fees'

    id = db.Column(db.Integer, primary_key=True)
    fee_no = db.Column(db.String(32), doc=u'费用唯一标识', unique=True)
    type = db.Column(db.String(12), doc=u'Optional 可选; Must 必选')
    name = db.Column(db.String(24), doc=u'费用名称')
    amount = db.Column(db.DECIMAL(12, 2), doc=u'金额')
    fee_desc = db.Column(db.String(128), doc=u'费用描述')
    sort = db.Column(db.Integer, doc=u'费用排序')
    image = db.Column(db.String(24), doc=u'该费用对应的图片')
    group = db.Column(db.String(32), doc=u'费用分组，同一个费用可能由多个费用组合，这里子项默认为单选')
    create_time = Column("create_time", DATETIME, nullable=False, default=datetime.now, doc=u'创建时间')
    update_time = Column("update_time", DATETIME, nullable=False, default=datetime.now, onupdate=datetime.now,
                         doc=u'更新时间')
    remark = db.Column(db.String(128), doc=u'备注')


class Order(Base):
    __tablename__ = 't_order'

    id = db.Column(db.Integer, primary_key=True)
    order_no = db.Column(db.String(32), doc=u'费用唯一标识', unique=True)
    student_no = db.Column(db.String(24), doc=u'学生学号')
    status = db.Column(db.String(24), doc=u'订单状态')
    pay_amt = db.Column(db.DECIMAL(12, 2), doc=u'支付金额')
    pay_time = Column("pay_time", DATETIME, nullable=True, doc=u'支付时间')
    create_time = Column("create_time", DATETIME, nullable=False, default=datetime.now, doc=u'创建时间')
    update_time = Column("update_time", DATETIME, nullable=False, default=datetime.now, onupdate=datetime.now,
                         doc=u'更新时间')
    remark = db.Column(db.String(128), doc=u'备注')


class TDTCFees(Base):
    __tablename__ = 't_tdtc_fees'

    id = db.Column(db.Integer, primary_key=True)
    fee_no = db.Column(db.String(32), doc=u'费用唯一标识')
    year = db.Column(db.String(8), doc=u'学年')
    fee_name = db.Column(db.String(32), doc=u'费用名称')
    student_no = db.Column(db.String(24), doc=u'学生学号')
    amt = db.Column(db.DECIMAL(12, 2), doc=u'欠费金额')
    loan_amt = db.Column(db.DECIMAL(12, 2), doc=u'贷款金额')
    detect_amt = db.Column(db.DECIMAL(12, 2), doc=u'减免金额')
    refund_amt = db.Column(db.DECIMAL(12, 2), doc=u'退款金额')
    paid_amt = db.Column(db.DECIMAL(12, 2), doc=u'已缴金额')
    fee_desc = db.Column(db.String(128), doc=u'缴费项目说明')
    begin_time = Column("begin_time", DATETIME, nullable=True, doc=u'开始缴费时间')
    end_time = Column("end_time", DATETIME, nullable=True, doc=u'缴费结束时间')
    create_time = Column("create_time", DATETIME, nullable=False, default=datetime.now, doc=u'创建时间')
    update_time = Column("update_time", DATETIME, nullable=False, default=datetime.now, onupdate=datetime.now,
                         doc=u'更新时间')
    remark = db.Column(db.String(128), doc=u'备注')

class OrderFees(Base):
    __tablename__ = 't_order_fees'

    id = db.Column(db.Integer, primary_key=True)
    order_no = db.Column(db.String(32), doc=u'订单唯一标识')
    fee_no = db.Column(db.String(32), doc=u'费用唯一标识')
    create_time = Column("create_time", DATETIME, nullable=False, default=datetime.now, doc=u'创建时间')
    update_time = Column("update_time", DATETIME, nullable=False, default=datetime.now, onupdate=datetime.now,
                         doc=u'更新时间')
    remark = db.Column(db.String(128), doc=u'备注')


class StudentLog(Base):
    __tablename__ = 't_student_log'

    id = db.Column(db.Integer, primary_key=True)
    student_no = db.Column(db.String(24), doc=u'学生学号')
    method = db.Column(db.String(24), doc=u'方法名称')
    req_data = db.Column(db.String(1024), doc=u'请求数据')
    resp_data = db.Column(db.String(1024), doc=u'响应数据')
    create_time = Column("create_time", DATETIME, nullable=False, default=datetime.now, doc=u'创建时间')
    update_time = Column("update_time", DATETIME, nullable=False, default=datetime.now, onupdate=datetime.now,
                         doc=u'更新时间')
    remark = db.Column(db.String(128), doc=u'备注')

