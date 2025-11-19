
GET_PRODUCTS = 'SELECT masp, tensp, gia, mota_sanpham, phantram_khuyenmai, ngay_tao, ma_dmc FROM sanpham'

GET_ORDER_STATUS = '''
SELECT 
    dh.ma_dh,          -- Mã đơn hàng
    dh.ngay_lap,       -- Ngày lập đơn
    dh.noi_giao,       -- Nơi giao hàng
    sp.tensp,          -- Tên sản phẩm
    ctdh.size,         -- Kích cỡ sản phẩm đã đặt
    ctdh.color,        -- Màu sắc sản phẩm đã đặt
    ctdh.soluong,      -- Số lượng
    ctdh.don_gia,      -- Đơn giá
    ctdh.thanh_tien,   -- Thành tiền cho mục này
    ctdh.trangthai     -- Trạng thái của mục này trong đơn hàng
FROM 
    donhang AS dh
-- Kết nối đến bảng chi tiết đơn hàng để lấy các sản phẩm
JOIN 
    chi_tiet_don_hang AS ctdh ON dh.ma_dh = ctdh.ma_dh
-- Kết nối đến bảng biến thể sản phẩm để lấy thông tin chi tiết
JOIN 
    sanphambt AS spbt ON ctdh.mabt = spbt.mabt
-- Kết nối đến bảng sản phẩm để lấy tên sản phẩm
JOIN 
    sanpham AS sp ON spbt.masp = sp.masp
WHERE 
    dh.makh = {user_id};
'''