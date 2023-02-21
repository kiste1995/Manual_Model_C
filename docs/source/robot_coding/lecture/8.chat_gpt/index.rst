ChatGPT
===========


Chat Generative Pre-Trained Transformer or ChatGPT is a model developed and trained by Open AI that interacts with users in a conversational way. 
The dialogue format allows ChatGPT to answer followup questions, admit its mistakes, challenge incorrect premises, and reject inappropriate requests.

Not only can it answer conversational questions, it can answer detailed questions from complex codes to many forms of literature. 

Sample 
-------

The following is a sample that asks ChatGPT to clarify questions to debug code. 

- **User**: this code is not working like I expect -- How do I fix it?
  
  .. code-block:: c

    resultWorkerErr := make(chan error)
    defer close(resultWorkerErr)
    go func() {
        defer cancel()
        resultWorkerErr <- b.resultWorker(ctx)
    }()

    err := b.worker(ctx)
    cancel()
    if err == nil {
        return <-resultWorkerErr
    }
    return multierror.Append(err, <-resultWorkerErr)

- **ChatGPT**: It’s difficult to say what’s wrong with the code without more context. Can you provide more information about what the code is supposed to do and what isn’t working as expected? Also, is this the entire code or just a part of it?
- **User**: just part of it — the error never surfaces. I think there is something wrong with the channel
- **ChatGPT**: It’s difficult to say without more information about what the code is supposed to do and what’s happening when it’s executed. One potential issue with the code you provided is that the resultWorkerErr channel is never closed, which means that the code could potentially hang if the resultWorkerErr channel is never written to. This could happen if b.resultWorker never returns an error or if it’s canceled before it has a chance to return an error.
  
  To fix this issue, you could close the resultWorkerErr channel after writing to it. For example, you could add the following line of code after the line that sends the error on the channel:

  .. code-block:: c

    close(resultworkerErr)

  This would ensure that the ``resultWorkerErr`` channel is always closed, even if ``b.resultWorker`` never returns an error. Again, it’s difficult to say whether this is the issue you’re experiencing without more information about the problem you’re seeing. Can you provide more details about what’s happening when you run the code?

Methods
---------

The ChatGPT is trained with Reinforcement Learning from Human Feedback (RLHF), using the same methods as InstructerGPT but with slight differences
in the data collection setup. The initial model was trained with supervised fine-tuning:

- This was done by human AI trainers providing converstions in which they played both the user and chatGPT sides. This was mixed with the 
  InstructerGPT dataset, whichwas transformed into a dialogue format. 

- The Reinforcement learning requires rewards system. To provide this system, the chatGPT had to have a comparison data, which consisted of two or more model responses ranked by quality. 
  For this task, data from conversation between AI trainers and chatbot was collected and was ranked. 

- With this reward models, the model was fine-tuned using Proximal Policy Optimization. This is repeated several times. 
  
.. thumbnail:: /_images/ai_training/ChatGPT_Diagram.svg

The fine tuning for ChatGPT was taken from a model in the GPT-3.5 series. These models were trained on an Azure AI supercomputing infrastructure.

Limitations
-------------

- In some cases, the ChatGPT does not produce sound and understandable responses. This problem is incredibly difficult to fix as:

    1. There are no source of truth during the Reinforcement Learning step.
    2. Setting the model to be more cautious forces the model to have limited range of responsiveness.
    3. Supervised learnings misleads the model, as the models ideal answer depends on what the model knows rather than what the human demonstrator knows. 

- ChatGPT is very sensitive as a quote with no solution may be tweaked in the smallest way to have correct response. 
- The model may become excessively verbose and overuses certain phrases.
- It is ideal for the model to clarify unclear questions from the user, but the current model assumes the question from the user. 
- Although it protects itself from producing harmful or inappropriate responses but it has some false negatives.  