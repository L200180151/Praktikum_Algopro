def luas(a, t):
    l = a * t * 0.5
    return l

print "<!DOCTYPE html>"
print
print"""<html>
        <head>
            <title>Kegiatan 3</title>
        </head>
        <body>
            <table border='0'>
                <tr>
                    <td colspan='4'><p align='center'><b>Bangun Segitiga</b></p></td>
                </tr>
                <tr>
                    <td rowspan='7'><img src='../segitiga.jpg'></td>
                </tr>
                <tr>
                    <td>Nama bangun</td>
                    <td>:</td>
                    <td>Segitiga</td>
                </tr>
                <tr>
                    <td>Dimensi</td>
                    <td>:</td>
                    <td>2D</tdd>
                </tr>
                <tr>
                    <td>Rumus Luas</td>
                    <td>:</td>
                    <td> 1/2 x Alas x Tinggi</td>
                </tr>
                <tr>
                    <td>Parameter 1</td>
                    <td>:</td>
                    <td>4 cm</td>
                </tr>
                <tr>
                    <td>Parameter 2</td>
                    <td>:</td>
                    <td>3 cm</td>
                </tr>
                <tr>
                    <td>Luas</td>
                    <td>:</td>
                    <td> """
print luas(4, 3)
print """cm</td>
                </tr>
            <table>
        </body>
    </html>"""
                    
                    
