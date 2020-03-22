{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "java -jar RankLib-patched.jar -test MQ2008/Fold2/test.txt -metric2T NDCG@10 -idv output/baseline.ndcg.txt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "RankNet: java -jar RankLib-patched.jar -train MQ2008/Fold2/train.txt -test MQ2008/Fold2/test.txt -validate MQ2008/Fold2/vali.txt -ranker 1 -metric2t NDCG@10 -metric2T NDCG@10 -save model_ranknet.txt\n",
    "ListNet: java -jar RankLib-patched.jar -train MQ2008/Fold2/train.txt -test MQ2008/Fold2/test.txt -validate MQ2008/Fold2/vali.txt -ranker 7 -metric2t NDCG@10 -metric2T NDCG@10 -save model_listnet.txt\n",
    "LambdaMart: java -jar RankLib-patched.jar -train MQ2008/Fold2/train.txt -test MQ2008/Fold2/test.txt -validate MQ2008/Fold2/vali.txt -ranker 6 -metric2t NDCG@10 -metric2T NDCG@10 -save model_lambdamart.txt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "RankNet: java -jar RankLib-patched.jar -load model_ranknet.txt -test MQ2008/Fold1/test.txt -metric2T NDCG@10 -idv output/ranknet.ndcg.txt    \n",
    "ListNet: java -jar RankLib-patched.jar -load model_listnet.txt -test MQ2008/Fold1/test.txt -metric2T NDCG@10 -idv output/listnet.ndcg.txt    \n",
    "LambdaMart: java -jar RankLib-patched.jar -load model_lambdamart.txt -test MQ2008/Fold1/test.txt -metric2T NDCG@10 -idv output/lambdamart.ndcg.txt    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "java -cp RankLib-patched.jar ciir.umass.edu.eval.Analyzer -all output/ -base baseline.ndcg.txt > analysis.txt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
