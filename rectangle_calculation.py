class RectangleCalculation:
    @staticmethod
    def calculate_perimeter(length, width):
        """
        计算矩形周长
        :param length: 矩形的长
        :param width: 矩形的宽
        :return:
        """
        if length < 0 or width < 0:
            return None
        if length == 0 or width == 0:
            return 0
        return 2 * (length + width)

    @staticmethod
    def calculate_area(length, width):
        """
        计算矩形面积
        :param length: 矩形的长
        :param width: 矩形的宽
        :return:
        """
        if length < 0 or width < 0:
            return None
        return length * width


if __name__ == '__main__':
    print("矩形的周长:{}".format(RectangleCalculation.calculate_perimeter(2, 4)))
    print("矩形的面积:{}".format(RectangleCalculation.calculate_area(2, 4)))