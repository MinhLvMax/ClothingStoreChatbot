
GET_PRODUCTS = 'SELECT masp, tensp, gia, mota_sanpham, phantram_khuyenmai, ngay_tao, ma_dmc FROM sanpham'

GET_ORDER_STATUS = """
SELECT 
    dh.ma_dh,
    dh.ngay_lap,
    dh.noi_giao,
    sp.tensp,
    ctdh.size,
    ctdh.color,
    ctdh.soluong,
    ctdh.don_gia,
    ctdh.thanh_tien,
    ctdh.trangthai
FROM donhang AS dh
JOIN chi_tiet_don_hang AS ctdh ON dh.ma_dh = ctdh.ma_dh
JOIN sanphambt AS spbt ON ctdh.mabt = spbt.mabt
JOIN sanpham AS sp ON spbt.masp = sp.masp
WHERE dh.makh = :user_id;
"""