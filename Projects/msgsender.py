nums=[9963926009,9391245688,9866271773,8328398248,8886155516,8121999955,9866615903,9246565648,9989979851,8008794580,9885044499,8374778385,7729075740,9949648195,7780325679,6281559283,8341888785,7993149018,9440258820,9030646711,9000081770,9848303573,9949296782,9885254199,9908109294,7674978431,9000363794,9989363239,9866964100,8978572055,9985066497,9246540993,7660861981,9985159267,9121086117,7660861981]

s="https://api.whatsapp.com/send?phone=91"
s1="&text=Hi%2C%20I%20am%20Aryan%20Keluskar%2C%20your%20student%20trainer%20for%20the%20Video%20Editing%20Club.%20Thanks%20for%20showing%20your%20interest%20in%20learning%20Video%20Editing.%20We%20will%20be%20using%20VN%20Video%20Editor%20throughout%20the%20course%2C%20so%20install%20it%20from%20Play%20Store%20or%20App%20Store.%20You%20will%20soon%20recieve%20an%20email%20with%20the%20Google%20Classroom%20invite.%0AClick%20to%20join%20the%20Whatsapp%20Group%3A%20https%3A%2F%2Fchat.whatsapp.com%2FJK2qe51BXGP9G8V4JZbYUG%0AFeel%20free%20to%20ask%20me%20any%20queries%20you%20face."
i=0
while(i<nums.__len__()):
    f=open("msg.txt","a")
    f.write(s+str(nums[i])+s1)
    f.write("\n\n")
    i=i+1
