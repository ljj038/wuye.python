#!/usr/bin/python
# -*- coding: utf-8 -*-


class htmlDrawer:
    def outPut(self, data):
        if(data is None):
            return False
        f = open('html/out.html', 'w')
        htmlHead = """
        <!DOCTYPE html>
        <html lang="zh-CN">
        <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>spider</title>
        <link rel="stylesheet" href="http://cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min.css">
        <!--[if lt IE 9]>
        <script src="http://cdn.bootcss.com/html5shiv/3.7.2/html5shiv.min.js"></script>
        <script src="http://cdn.bootcss.com/respond.js/1.4.2/respond.min.js"></script>
        <![endif]-->
        </head>
        <body>
        <script src="http://cdn.bootcss.com/jquery/1.11.3/jquery.min.js"></script>
        <script src="http://cdn.bootcss.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
        <div class="container" style="margin-top:50px">
        <div class="row">
        <div class="col-xs-12 col-sm-12 col-md-12">
        <table class="table table-bordered table-striped table-responsive">
        <thead>
        <tr>
        <th class="text-center">title</th>
        <th class="text-center">summary</th>
        </tr>
        </thead>
        <tbody>
        """

        htmlFoot = """
        </tbody>
        </table>
        </div>
        </div>
        </div>
        """
        f.write(htmlHead)

        for content in data:
            if(
                (content.get('summary', None) != None)  and
                (content.get('title', None) != None)
            ):
                f.write('<tr>')
                f.write('<td class="text-center">%s</td>' % (content['title'].encode('utf-8')))
                f.write('<td>%s</td>' % (content['summary'].encode('utf-8')))
                f.write('</tr>')

        f.write(htmlFoot)
        f.close()
