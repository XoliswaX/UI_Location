from flask import Blueprint, render_template, jsonify, request

home= Blueprint("home",__name__)

@home.route('/',methods=['GET', 'POST'])

def homePage():
     return render_template("index.html")