from flask import Flask, request, redirect, render_template, url_for, flash, jsonify
from main.utility.pagination import pagination
from main import app, db
import os
from .models import Product
@app.route('/', methods=['GET'])
def admin_page():
    return render_template('product_listing.html')

@app.route('/ajax-listing', methods=['POST'])
def ajax_product_listing():
    if(request.form['Submit'] == 'Pagination'):
        data = {}
        numofrecords = request.form['numofrecords']
        page = request.form['page']
        Limitpage = int(page)-1
        start = int(Limitpage) * int(numofrecords)
        numofrecords = int(numofrecords)
        data['Limitpage'] = numofrecords
        data['start'] = start
        product_list = Product.get_product_list(data, 'select')
        num_rows = Product.get_product_list(data, 'count')
        if(product_list):
            msg = ''
            key_num = int(numofrecords) * (int(page)-1)
            for pro in product_list:
                key_num += 1
                msg += '<tr>'
                msg += '<td>'+str(key_num)+'</td >'
                msg += '<td>'+pro['first_name']+'</td >'
                msg += '<td>'+pro['last_name']+'</td >'
                msg += '<td>'+pro['pet_name']+'</td >'
                msg += '<td>'+pro['email']+'</td >'
                msg += '<td>'+pro['gender']+'</td >'
                msg += '<td>'+pro['ip_address']+'</td >'
                msg += '</tr>'
            msg += '<tr><td colspan="24">'+pagination(numofrecords, num_rows, page)+'</td></tr>'
        else:
            msg += '''< tr >
                    <td colspan = "24" style = "text-align: center; color: red;" > No data Found < /td >
                 </tr>'''
        response = {
            'message': msg
        }
        return jsonify(response), 201
