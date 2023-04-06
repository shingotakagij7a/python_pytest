import pytest

from app.int_triangle import IntTriangle


@pytest.fixture
def triangle():
    return IntTriangle(1, 1, 1)


class TestIntTriangle:
    class Test_constructor:
        class Test_3つの入力がすべて正の整数で三角形の条件を満たす場合にインスタンス作成に成功する:
            def test_1_1_1の場合(self, triangle):
                assert triangle.side_a == 1
                assert triangle.side_b == 1
                assert triangle.side_c == 1

        class Test_3つの入力のうち1つでも正の整数でない場合に三角形のインスタンス作成に失敗する:
            def test_0を含む場合(self):
                with pytest.raises(ValueError, match="Input must be positive"):
                    IntTriangle(0, 0, 0)

            def test_負の数を含む場合(self):
                with pytest.raises(ValueError, match="Input must be positive"):
                    IntTriangle(-1, 1, 1)

            def test_小数を含む場合(self):
                with pytest.raises(ValueError, match="Input must be integer"):
                    IntTriangle(0.1, 1, 1)

        class Test_3つの入力が三角形の条件を満たさない場合に三角形のインスタンス作成に失敗する:
            def test_1辺の長さが他の2辺の和より小さくない場合(self):
                with pytest.raises(
                    ValueError, match="Input must meet triangle condition"
                ):
                    IntTriangle(1, 1, 2)

    class Test_perimeter:
        class Test_3辺の値の合計を整数値で返す:
            def test_1_1_1の場合(self, triangle):
                assert triangle.perimeter() == 3

    class Test_area:
        class Test_面積を小数点第2位を四捨五入した小数値で返す:
            def test_1_1_1の場合(self, triangle):
                assert triangle.area() == 0.4

            def test_3_4_5の場合(self):
                triangle = IntTriangle(3, 4, 5)
                assert triangle.area() == 6.0
