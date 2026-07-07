# Cath

Cath Overall Accuracy \- 72.1%   
Cath Overall Accuracy removing Q7 (see reason below) \- 78.33%

Q1: How do alternative packaging materials compare to plastic for you? \- 76% match

1. The confidence level of the real answer is mid at best. Simulated is obviously 100%. I understand confidence prediction is nearly impossible, but it would matter in simulation so I'm a bit on the fence here.  
2. Cath mentioned “I would like to make the right choice but I'm not 100% sure what the right choice is.” which is key to her answer, but is not a part of ours and to a degree cannot be \-\> how do we handle this in accuracy matching?

Q2: What are your views on the environmental impact of plastic food packaging? \- 63%

1. I think except the overall sentiment (which is negative) the reasoning is completely out of place b/w our simulated answer and real answer here. Cath’s actual answer is centred around the broader political and social scenario, whereas our answer focuses on packaging.   
2. Now, it also seems unlikely that we will ever be able to predict political reasons here. It has not been covered before. The simulation is very much in line with whatever has been covered before, but maybe it is an unfair question to consider then. \-\> I am confused.  
3. We might need to weigh the accuracy % down depending on how we are judging this. 63% seems high to me if the why is wrong in a qualitative answer simulation. 

Q3: How confident are you that you know the “right” packaging choice? \- 92%

1. This seems encouraging \- the LLM predicted low confidence here.

Q4: When do you compromise or make exceptions on plastic use? \- 58%

1. Here the only difference between actual answer and simulated answer is the number of examples Cath has given. This I think can be eliminated as an accuracy criteria as long as the answer and its reasoning and feeling is same (which it is)  
2. ~~Other than that, since simulations gave two examples, I checked and saw those instances are mentioned in the diary (obviously) \- does this make it a biased question?~~ 

Q5: How does food waste or freshness affect your packaging/shopping choices? \- 81%

1. This is interesting. Her answer is in a nutshell \- “I try to avoid both plastic and food waste through meticulous meal planning, but I honestly don't know which evil is worse so please just tell me the right choices so I can stop worrying I'm doing the environmentally conscientious thing wrong.” which has three components \- meal planning, lack of knowledge, strong environmental concerns  
2. Now, our answer is \- “It affects my choices all the time, really. Because there are only two of us, I meal-plan, shop little and often, and freeze things like bread, milk and leftovers so we don’t end up throwing food away; and I avoid things like bagged salad because that’s one of the few things I know can go slimy very quickly and get wasted. Sometimes I’ll tolerate packaging if I think it genuinely helps something keep fresh for longer, but I’d still rather buy loose and only buy the amount I know we’ll use.” which kind of covers meal planning and strong environmental concerns only.  
3. Also, the tone is different \-\> now I am not sure how to weigh this here.   
4. I also think 81% is higher than what it should have been scored? 

Q6: Does packaging influence what you buy? \- 100%

1. Yarr isme fir wahi, way too much grounding on one example. It just feels like overfitting right now.   
2. The actual answer is more about-   
   1. prefers cardboard/paper over plastic because it feels safer if recycling fails (it breaks down instead of becoming microplastics),   
   2. but she’s stuck in a loop of conflicting information, defaults to avoiding plastic anyway, and sees growing your own food as the only way to truly escape the packaging dilemma.  
   3. I try to avoid the plastic if I can but I still, as you saw when you came to my house, I still end up with a mountain of it.  
3. Our answer is \- “Yes, all the time. I’ll often choose loose fruit and veg, or use the Waitrose Unpacked section, and I’ve definitely bought individual peppers rather than a cheaper plastic-wrapped pack because I don’t want the packaging. But it’s a constant trade-off with organic, price and convenience, so sometimes I still end up buying the packaged version and feeling a bit guilty about it.”  
4. Our answer is heavily indexed on instances in the diary and not the overall sentiment which is being asked of?

Q7: Who should be responsible for reducing plastic? \- 35%

1. Well, I think I did not choose the actual answer correctly here or it doesn’t exist. We can remove this for Cath now. The actual answer is about her social circle and how it correlates with environmental awareness and not really who should be responsible xyz.

# Eliza

Eliza Overall Accuracy \- 72.1%   
Eliza Overall Accuracy removing Q4 (see reason below) \- 73.6%

Q1: How do alternative packaging materials compare to plastic for you? \- 28%

1. Umm, so, the real answer is very contextual to the questions before and after in that conversation. (which is why it is different from what we predicted)  
2. Having said that, the simulated response makes much more sense than Eliza’s turtle rant here. So, it’s a not-so-classic say-do gap situation? Idk what we should do here. 

Q2: What are your views on the environmental impact of plastic food packaging? \- 64%

1. Well, she never really answered the question in depth and focused on packaging. But, we cannot change it as well?   
2. So I guess, it is what it is here? Or is it another say-do gap situation?

Q3: How confident are you that you know the “right” packaging choice? \- 92%

1. Sims predicted mixed confidence with the right reasoning\!   
2. Want to benchmark this question against synthetics 

Q4. When do you compromise or make exceptions on plastic use? \- 58%

1. I chose the wrong answer here. The original question is “Research says plastic packaging can keep food fresher — how do you weigh that against plastic waste?” we need to skip this question for Eliza

Q5: How does food waste or freshness affect your packaging/shopping choices? \- 84%

1. Again, everything was mentioned in her previous diaries, so this is pretty much a summary and not predicted behaviour \- so is it biased or not?  
2. Also the simulated answer kind of misses the key reasoning in the actual answer \- that for her food waste is much worse than plastic pollution, so 84% accuracy also seems a bit higher. 

Q6: Does packaging influence what you buy? \- 100%

1. Again, I have fucked up the answer here \- but it is a bit convoluted.   
2. Overall, it looks okay \- can keep for now. 

# Ella

Ella Overall Accuracy \- 71%   
This participant has some obvious issues, we might need to keep this out.

Q1: How do alternative packaging materials compare to plastic for you? \- 91%

1. I messed up here. There is no direct evidence to this question in her transcript.   
2. But, if you can take: “ "In week 3 diary you audited unnecessary plastic packaging — why is paella rice packaging unnecessary?"“, the answer is- “So when it comes in a plastic packet that packet is going to sit around for a really long time, because it won't get recycled. But with, you can just change the packaging, you could have it in a cardboard box because they're dry products that its not going to affect the quality of the product if its in a carboard box or if its in a glass jar. And these products are recyclable and they're easy to recycle. So that's why I would say that the plastic is unnecessary because its causing unnecessary sort of waste/pollution.”  
3. But overall, I think that we may have to skip this one for Ella. Although the simulated answer is almost a 100% match to \#2

Q2: What are your views on the environmental impact of plastic food packaging? \- 63%

1. Well, she never really answered the question in depth and focused on packaging. But, we cannot change it as well?   
2. So I guess, it is what it is here? Or is it another say-do gap situation?

Q3: How confident are you that you know the “right” packaging choice? \- 94%

1. I have not chosen the right answer in hindsight here. The challenge is this question is not exactly in the transcript, but more like a mix of the following questions:  
   1. What do you mean when you say glass and cardboard are more recyclable than plastic?  
   2. Did plastic packaging affect your decision to buy reduced udon noodles?  
   3. Was there an appeal to buying loose tea leaves?  
   4. In Interview 1 you preferred packaged snacks over fruit — what draws you to those snacks?  
2. And therefore, it might have to be a mix of these \- where I would need a bit of judgement call from a third party.   
3. Having said that, the simulated answer looks pretty on point to me with the transcripts, but has the same information bias. 

Q4. When do you compromise or make exceptions on plastic use? \- 18%

1. This question has the same issue as Q3. Essentially, it is the same question in Ella’s context.   
2. Having said that, the accuracy should not have been at extreme ends. It is so because Ella’s answer is a bit controversial here. She said “Yeah, I don't think I've thought much about the plastic when I was buying it, just more so when I was reflecting, looking through all of the cupboards for that diary entry, its something that I thought about.” \-\> and therefore negated her environment friendliness.  
3. So, let’s take a judgement call here as well. I think Ella as a participant is pretty disqualified to me right now.    
   

Q5: How does food waste or freshness affect your packaging/shopping choices? \- 91%

1. Again, I might have to club more answers here. I think only the snacks vs fruits answer is here when she answers to “In Interview 1 you preferred packaged snacks over fruit — what draws you to those snacks?”  
2. I purposefully did not club because otherwise all the answers would be the same. But at this point idk how to read this anymore. 

Q6: Does packaging influence what you buy? \- 100%

1. Same issue as Q5. took only one answer of “Was there an appeal to buying loose tea leaves?”

Q7: Who should be responsible for reducing plastic? \- 42%

1. So, towards the end and the actual answer her conclusion is \-   
   1. Consumers need to become eco-conscious and change what they buy.  
   2. Corporations only change when consumer demand forces them to.  
2. But before the interview, her views are that more corporations are bad and force it upon us \- which is what the simulation has predicted.  
3. I included this question keeping artificial societies and Aaru in mind, but I guess it makes sense only on a larger scale. 

# Isabella

Isabella Overall Accuracy \- 68%   
Isabella Overall Accuracy removing Q5 (see reason below) \- 73.5%

Q1: How do alternative packaging materials compare to plastic for you? \- 42%

1. This question has the standard LLM is too confident issue.  
2. Apart from that everything is correct, barring the examples which imo should not be an accuracy criteria unlike now.  

Q2: What are your views on the environmental impact of plastic food packaging? \- 82%

1. The LLM went for % accuracy match here, not what matters the most in the question’s context. If we keep that away, it should be a 95%+ match.  
   

Q3: How confident are you that you know the “right” packaging choice? \- 94%

1. Sims predicted mixed confidence with the right reasoning\!   
2. Want to benchmark this question against synthetics 

Q4. When do you compromise or make exceptions on plastic use? \- 58%

1. She chose an analogy here and not an actual answer.   
2. I wanted to see what would happen, but in hindsight, maybe this needs to be skipped as it is not tied to the objective?

Q5: How does food waste or freshness affect your packaging/shopping choices? \- 38%

1. Need to skip this for Isabella, she did not get asked about freshness with packaging choices directly nor did she answer.  
2. We can draw indirect conclusions (which was my hope initially)  but it is too convoluted. 

Q6: Does packaging influence what you buy? \- 100%

1. No problems here \- binary outcome, reasoning, and exceptions are correct\! 

Q7: Who should be responsible for reducing plastic? \- 65%

1. So, I don’t think this deserves a 65% accuracy match. The actual answer is pretty much “individual” and simulated answer is pretty much “corporation”  
2. The reasoning is also very different. The actual answer is \- “individuals being conscious of that and as a collective being also willing to protest and letting the people higher know that we want change to be made.” The simulated answer is \- “I think individuals should try to do their part, of course, but the main responsibility is on supermarkets, companies and the institutions that make the system, because they decide the packaging and whether recycling is actually possible.”  
3. Again, this is a very philosophical question and I wanted to experiment so we can remove it if you all feel so. 

# Jacob

Jacob Overall Accuracy \- 51%   
Jacob Overall Accuracy removing Q4 (see reason below) \- 52.16%

Q1: How do alternative packaging materials compare to plastic for you? \- 12%

1. Well, this is some major level fuck up here. The simulated answer is quite opposite to the views in the actual answer.   
2. But, the views in the simulated answer are decently in-line with the diaries and previous interview. But this doesn’t feel like a strong reason to eliminate.   
3. So, it’s a not-so-classic say-do gap situation again? Idk what we should do.

Q2: What are your views on the environmental impact of plastic food packaging? \- 78%

1. Now, interestingly the actual answer to both \#1 and \#2 are the same, but the responses framing differs a lot, and therefore it matches much better.  
2. It is also because the question-answers are more well tied together here.   
   

Q3: How confident are you that you know the “right” packaging choice? \- 63%

1. Actually both the actual answer and simulated answer are pretty similar (90%+) barring the extremely different examples taken.  
2. However, the actual response is mainly about skepticism and curiosity, while the predicted response is about recognizing packaging materials for disposal, so the core stance overlaps but the key insight differs. But is it as bad as say a 37% gap considering the overall objective and transcript? Idts.

Q4. When do you compromise or make exceptions on plastic use? \- 42%

1. This question needs to be skipped for Jacob in hindsight.

Q5: How does food waste or freshness affect your packaging/shopping choices? \- 18%

1. This is tricky. Jacob rejects the idea that plastic packaging is justified because it reduces food waste \+ focuses on recycling.  
2. The simulation took the question in a different direction and focuses on batch size and reuse.  
3. Now \#2 seems more logical than \#1 but at the same time is relative?

Q6: Does packaging influence what you buy? \- 100%

1. No problems here

Q7: Who should be responsible for reducing plastic? \- 42%

1. This has a major issue \- the actual answer is pretty much “producer to consumers” and simulated answer is pretty much “individual \+ government”  
2. The core reasoning on why “not just individuals” is the same though.