import rclpy
from rclpy.node import Node
import smbus2
import time

class I2CSender(Node):
    def __init__(self):
        super().__init__('position_sender')
        self.bus = smbus2.SMBus(1)  # 使用I2C-1接口
        self.slave_address = 0x54  # STM32的从机地址

        # 创建定时器，每隔0.01秒(10ms)发送一次数据
        self.timer = self.create_timer(0.01, self.send_data)


    def send_data(self):
        try:
            # 示例数据：前4个字节为有效数据，后4个字节为0
            # data = [0x00, 0x01, 0x02, 0x03, 0x00, 0x00, 0x00, 0x00]
            # 第一字节为特征标头
            # 第二字节为状态码(0x00:能确认自身位置, 0x01:无法确认自身位置)
            # 第三字节为场地X坐标
            # 第四字节为场地Y坐标
            # 第五字节为目标X坐标
            # 第六字节为目标Y坐标
            # 第七字节为0
            # 第八字节为0

            data = []

            # 发送数据
            self.bus.write_i2c_block_data(self.slave_address, 0, data)
            self.get_logger().info(f'Sent data: {data}')
        except Exception as e:
            self.get_logger().error(f'Error sending data: {e}')

def main(args=None):
    rclpy.init(args=args)
    i2c_sender = I2CSender()
    rclpy.spin(i2c_sender)
    i2c_sender.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()