#!/usr/bin/python
# -*- encoding: utf-8 -*-

from app.controller.admin import admin
from flask import request, current_app as app, url_for
from flask_login import login_required
from app import db
from app.models.CommonModel import BannerCfg
from app.utils.Upload import Upload

from app.utils.restful_response import CommonResponse, ResultType
from sqlalchemy import or_




@admin.route('/upload', methods=['POST'])
def upload():
    upload= Upload()
    pic_path = upload.upload_file()
    return CommonResponse(ResultType.Success, message=u"获取成功", data={"img_path":url_for('static',
            filename=pic_path,_external=True)}).to_json()



@admin.route('/add_banner', methods=['GET', 'POST'])
@login_required
def add_banner():
    try:
        title = request.form.get('title')
        description = request.form.get('description')
        img_url = request.form.get('img_url')
        sort = request.form.get('sort')
        href = request.form.get('href')

        banner = BannerCfg()
        banner.title = title
        banner.href = href
        banner.description = description
        banner.img_url = img_url
        banner.sort = sort
        db.session.add(banner)
        db.session.commit()

        return CommonResponse(ResultType.Success, message=u"添加成功",).to_json()
    except Exception, e:
        app.logger.info(e)
    return CommonResponse(ResultType.Failed, message=u"编辑出现错误").to_json()


@admin.route('/edit_banner', methods=['GET', 'POST'])
@login_required
def edit_banner():
    try:
        banner_id = request.form.get('banner_id')
        title = request.form.get('title')
        description = request.form.get('description')
        href = request.form.get('href')
        img_url = request.form.get('img_url')
        sort = request.form.get('sort')
        banner = db.session.query(BannerCfg).filter(
            BannerCfg.id == banner_id
        ).first()
        banner.title = title
        banner.description = description
        banner.href = href
        banner.img_url = img_url
        banner.sort = sort
        db.session.merge(banner)
        db.session.commit()
        return CommonResponse(ResultType.Success, message=u"编辑成功").to_json()
    except Exception, e:
        app.logger.info(e)
    return CommonResponse(ResultType.Failed, message=u"编辑出现错误").to_json()

@admin.route('/del_banner', methods=['GET', 'POST'])
@login_required
def del_banner():
    try:
        banner_id = request.form.get('banner_id')

        db.session.query(BannerCfg).filter(
            BannerCfg.id == banner_id
        ).delete()
        db.session.commit()
        return CommonResponse(ResultType.Success, message=u"删除成功",).to_json()
    except Exception, e:
        app.logger.info(e)
    return CommonResponse(ResultType.Failed, message=u"删除Banner出现错误").to_json()

@admin.route('/get_banner_info', methods=['GET', 'POST'])
@login_required
def get_banner_info():
    try:
        banner_id = request.form.get('banner_id')

        data = db.session.query(BannerCfg).filter(
            BannerCfg.id == banner_id
        ).first()
        return CommonResponse(ResultType.Success, message=u"获取成功",data=data.to_json()).to_json()
    except Exception, e:
        app.logger.info(e)
    return CommonResponse(ResultType.Failed, message=u"获取成功Banner出现错误").to_json()

