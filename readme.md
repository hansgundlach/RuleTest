# A Study of Faithfulness in LLM Classification 

This is code provided to test the faithfulnes of models in a classification task. FrozenExamples contains the the frozen examples classifications used in-context for some of our measures. Examples were also generated programmaticly using gen_flag_examples, and gen_code_example methods. rulepipe.py runs most of the experimenets used in our paper. 

Task 1: Determine if a majority of letters in a string are 'b' or 'c'. This is a simple task that is easy to generate. It also easy to compare models peformance with different levels of b's and c's. Suprising the model is able to do the simplest version of the task almost perfectly with few examples.  However, without a larger number of in-context examples it is not able to state the more general rule. 

Task 2: Determine if a given statement has a hideen flag (ie set of capitalized letters). In this case we add the hidden flag to a series of text. In many cases the model thinks its reasoning is based on a complex heursitict of the provided text. However, it is able to succesfully classify text regardless of these rules suggesting it finds the flag more salient then it recognizes. 

Task 3 (Not fully investigated): We have done an intital investigation of the parantheis balancing task. Paranthesis balancing is a particulary informative task. In order, for the model to correclty balance paranthesis. It has to both check for the absolute number of open and closed paranthesis as well as the horizon (see xxxxxx). Initial results point to the fact that the model says it is doing the paran-balancing task while only doing one of the two subtasks. In general the model performs quite well on each subtask but cannot do the general task.  

Changing Prompt and Examples: It is possible to give the model a set of examples which give it the corrrect prompt to reason by. If these examples are not given the model will still reason accroding to the correct general form but will not be able to articulate its reasoning. Overall, we saw wide variation given based on the number and makeup of examples given in context. 
