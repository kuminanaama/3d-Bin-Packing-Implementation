class Box:
    def __init__(self,
                 box_id:str,
                 length:float,width:float,height:float):

        if not box_id.strip():
            raise ValueError("Box ID can't be empty")


        if length <= 0 or width <=0 or height<= 0 :
            raise ValueError("Box dimensions must be greater than zero")


        self.box_id = box_id
        self.length = length
        self.width = width
        self.height = height

    def volume(self) -> float:
        return self.length * self.width * self.height
    